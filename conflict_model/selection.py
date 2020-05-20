import pandas as pd
import geopandas as gpd
import numpy as np
import os, sys

def filter_conflict_properties(gdf, config):
    """filters conflict database according to certain conflict properties such as number of casualties, type of violence or country.

    Arguments:
        gdf {geodataframe}: geodataframe containing entries with conflicts
        config {configuration}: parsed configuration settings

    Returns:
        geodataframe: geodataframe containing filtered entries
    """    
    
    selection_criteria = {'best': config.getint('conflict', 'min_nr_casualties'),
                          'type_of_violence': config.getint('conflict', 'type_of_conflict'),
                          'country': config.get('conflict', 'country')}
    
    print('filtering on conflict properties...')
    
    for key in selection_criteria:

        if selection_criteria[key] == '':
            print('...passing key', key, 'as it is empty')
            pass

        elif isinstance(selection_criteria[key], (int)):
            if key == 'type_of_violence':
                print('...filtering key', key, 'with value', selection_criteria[key])
                gdf = gdf.loc[(gdf[key] == selection_criteria[key])]
            else:
                print('...filtering key', key, 'with lower value', selection_criteria[key])
                gdf = gdf.loc[(gdf[key] >= selection_criteria[key])]

        elif (isinstance(selection_criteria[key], (str))):
            print('...filtering key', key, 'with value', selection_criteria[key] + os.linesep)
            gdf = gdf.loc[(gdf[key] == selection_criteria[key])]

    return gdf

def select_period(gdf, config):
    """Reducing the geodataframe to those entries falling into a specified time period.

    Arguments:
        gdf {geodataframe}: geodataframe containing entries with conflicts
        config {configuration}: parsed configuration settings

    Returns:
        geodataframe: geodataframe containing filtered entries
    """    

    t0 = config.getint('settings', 'y_start')
    t1 = config.getint('settings', 'y_end')
    
    print('focussing on period between', t0, 'and', t1)
    print('')
    
    gdf = gdf.loc[(gdf.year >= t0) & (gdf.year <= t1)]
    
    return gdf

def clip_to_continent(gdf, config):
    """As the original conflict data has global extent, this function clips the database to those entries which have occured on a specified continent.

    Arguments:
        gdf {geodataframe}: geodataframe containing entries with conflicts
        config {configuration}: parsed configuration settings

    Returns:
        geodataframe: geodataframe containing filtered entries
        geodataframe: geodataframe containing country polygons of selected continent
    """    
    
    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    continent_gdf = world[world["continent"] == config.get('settings', 'continent')]
    
    print('clipping dataset to continent', str(config.get('settings', 'continent')) + os.linesep)
    
    gdf = gpd.clip(gdf, continent_gdf)
    
    return gdf, continent_gdf

def climate_zoning(gdf, config):
    """Only those conflicts falling in certain climate zones may be of interest and this functions keeps only those falling into the specified zones.

    Arguments:
        gdf {geodataframe}: geodataframe containing entries with conflicts
        config {configuration}: parsed configuration settings

    Returns:
        geodataframe: geodataframe containing filtered entries
    """    
    
    Koeppen_Geiger_fo = os.path.join(config.get('general', 'input_dir'),
                                     config.get('climate', 'shp')) 
    
    code2class_fo = os.path.join(config.get('general', 'input_dir'),
                                 config.get('climate', 'code2class'))
    
    look_up_classes = config.get('climate', 'zones').rsplit(',')
    
    KG_gdf = gpd.read_file(Koeppen_Geiger_fo)
    code2class = pd.read_csv(code2class_fo, sep='\t')
    
    code_nrs = []
    for entry in look_up_classes:
        code_nr = int(code2class['code'].loc[code2class['class'] == entry])
        code_nrs.append(code_nr)
    
    print('clipping to climate zones' + os.linesep)
    KG_gdf = KG_gdf.loc[KG_gdf['GRIDCODE'].isin(code_nrs)]
    
    if KG_gdf.crs != 'EPSG:4326':
        KG_gdf = KG_gdf.to_crs('EPSG:4326')

    gdf = gpd.clip(gdf, KG_gdf.buffer(0))
    
    return gdf

def select(gdf, config, plotting=False):
    """Filtering the original global conflict dataset based on a) conflict properties, b) time period, c) continent, and d) climate zone.

    Arguments:
        gdf {geodataframe}: geodataframe containing entries with conflicts
        config {configuration}: parsed configuration settings

    Keyword Arguments:
        plotting {bool}: whether or not to plot the resulting selection (default: False)

    Returns:
        geodataframe: geodataframe containing filtered entries
        geodataframe: geodataframe containing country polygons of selected continent
    """    

    gdf = filter_conflict_properties(gdf, config)

    gdf = select_period(gdf, config)

    gdf, continent_gdf = clip_to_continent(gdf, config)

    gdf = climate_zoning(gdf, config)

    # if specified, plot the result
    if plotting:
        print('plotting result' + os.linesep)
        ax = continent_conflict_gdf.plot(figsize=(10,5), legend=True, label='PRIO/UCDP events')
        continent_gdf.boundary.plot(ax=ax, color='0.5', linestyle=':')
        plt.legend()
        ax.set_xlim(continent_gdf.total_bounds[0]-1, continent_gdf.total_bounds[2]+1)
        ax.set_ylim(continent_gdf.total_bounds[1]-1, continent_gdf.total_bounds[3]+1)

    return gdf, continent_gdf