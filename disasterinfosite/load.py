import os
from django.contrib.gis.utils import LayerMapping


######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadMappings
EQ_Liquefact_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQ_Nisqual68_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQ_SeattleFault72_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQ_Tsunami_SeaFault72_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQ_URM_DensityZones_seattle_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Fire_WUI_kingco_only_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_100yr_wUrban_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_500yr_wUrban_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_CMZ_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_DamInundation_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_nearest_sand_distr_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Hubs_Nearest_seattle_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

LSLD_ExistingAreas_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

LSLD_Prone_kingco_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Volcano_Lahar_kingco_mapping = {
    'lookup_val': 'Lookup_val',
    'geom': 'MULTIPOLYGON'
}


EQ_Liquefact_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_Liquefact_kingco.shp'))
EQ_Nisqual68_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_Nisqual68_kingco.shp'))
EQ_SeattleFault72_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_SeattleFault72_kingco.shp'))
EQ_Tsunami_SeaFault72_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_Tsunami_SeaFault72_kingco.shp'))
EQ_URM_DensityZones_seattle_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_URM_DensityZones_seattle.shp'))
Fire_WUI_kingco_only_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Fire_WUI_kingco_only.shp'))
Flood_100yr_wUrban_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Flood_100yr_wUrban_kingco.shp'))
Flood_500yr_wUrban_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Flood_500yr_wUrban_kingco.shp'))
Flood_CMZ_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Flood_CMZ_kingco.shp'))
Flood_DamInundation_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Flood_DamInundation.shp'))
Flood_nearest_sand_distr_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Flood_nearest_sand_distr.shp'))
Hubs_Nearest_seattle_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Hubs_Nearest_seattle.shp'))
LSLD_ExistingAreas_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/LSLD_ExistingAreas_kingco.shp'))
LSLD_Prone_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/LSLD_Prone_kingco.shp'))
Volcano_Lahar_kingco_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Volcano_Lahar_kingco.shp'))
# END OF GENERATED CODE BLOCK
######################################################


def run(verbose=True):

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadGroups
    from .models import ShapefileGroup
    quake = ShapefileGroup.objects.get_or_create(name='quake')
    fire = ShapefileGroup.objects.get_or_create(name='fire')
    flood = ShapefileGroup.objects.get_or_create(name='flood')
    landslide = ShapefileGroup.objects.get_or_create(name='landslide')
    volcano = ShapefileGroup.objects.get_or_create(name='volcano')
# END OF GENERATED CODE BLOCK
######################################################

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadImports
    from .models import EQ_Liquefact_kingco
    lm_EQ_Liquefact_kingco = LayerMapping(EQ_Liquefact_kingco, EQ_Liquefact_kingco_shp, EQ_Liquefact_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_Liquefact_kingco.save(strict=True, verbose=verbose)

    from .models import EQ_Nisqual68_kingco
    lm_EQ_Nisqual68_kingco = LayerMapping(EQ_Nisqual68_kingco, EQ_Nisqual68_kingco_shp, EQ_Nisqual68_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_Nisqual68_kingco.save(strict=True, verbose=verbose)

    from .models import EQ_SeattleFault72_kingco
    lm_EQ_SeattleFault72_kingco = LayerMapping(EQ_SeattleFault72_kingco, EQ_SeattleFault72_kingco_shp, EQ_SeattleFault72_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_SeattleFault72_kingco.save(strict=True, verbose=verbose)

    from .models import EQ_Tsunami_SeaFault72_kingco
    lm_EQ_Tsunami_SeaFault72_kingco = LayerMapping(EQ_Tsunami_SeaFault72_kingco, EQ_Tsunami_SeaFault72_kingco_shp, EQ_Tsunami_SeaFault72_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_Tsunami_SeaFault72_kingco.save(strict=True, verbose=verbose)

    from .models import EQ_URM_DensityZones_seattle
    lm_EQ_URM_DensityZones_seattle = LayerMapping(EQ_URM_DensityZones_seattle, EQ_URM_DensityZones_seattle_shp, EQ_URM_DensityZones_seattle_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_URM_DensityZones_seattle.save(strict=True, verbose=verbose)

    from .models import Fire_WUI_kingco_only
    lm_Fire_WUI_kingco_only = LayerMapping(Fire_WUI_kingco_only, Fire_WUI_kingco_only_shp, Fire_WUI_kingco_only_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Fire_WUI_kingco_only.save(strict=True, verbose=verbose)

    from .models import Flood_100yr_wUrban_kingco
    lm_Flood_100yr_wUrban_kingco = LayerMapping(Flood_100yr_wUrban_kingco, Flood_100yr_wUrban_kingco_shp, Flood_100yr_wUrban_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_100yr_wUrban_kingco.save(strict=True, verbose=verbose)

    from .models import Flood_500yr_wUrban_kingco
    lm_Flood_500yr_wUrban_kingco = LayerMapping(Flood_500yr_wUrban_kingco, Flood_500yr_wUrban_kingco_shp, Flood_500yr_wUrban_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_500yr_wUrban_kingco.save(strict=True, verbose=verbose)

    from .models import Flood_CMZ_kingco
    lm_Flood_CMZ_kingco = LayerMapping(Flood_CMZ_kingco, Flood_CMZ_kingco_shp, Flood_CMZ_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_CMZ_kingco.save(strict=True, verbose=verbose)

    from .models import Flood_DamInundation
    lm_Flood_DamInundation = LayerMapping(Flood_DamInundation, Flood_DamInundation_shp, Flood_DamInundation_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_DamInundation.save(strict=True, verbose=verbose)

    from .models import Flood_nearest_sand_distr
    lm_Flood_nearest_sand_distr = LayerMapping(Flood_nearest_sand_distr, Flood_nearest_sand_distr_shp, Flood_nearest_sand_distr_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_nearest_sand_distr.save(strict=True, verbose=verbose)

    from .models import Hubs_Nearest_seattle
    lm_Hubs_Nearest_seattle = LayerMapping(Hubs_Nearest_seattle, Hubs_Nearest_seattle_shp, Hubs_Nearest_seattle_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Hubs_Nearest_seattle.save(strict=True, verbose=verbose)

    from .models import LSLD_ExistingAreas_kingco
    lm_LSLD_ExistingAreas_kingco = LayerMapping(LSLD_ExistingAreas_kingco, LSLD_ExistingAreas_kingco_shp, LSLD_ExistingAreas_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_LSLD_ExistingAreas_kingco.save(strict=True, verbose=verbose)

    from .models import LSLD_Prone_kingco
    lm_LSLD_Prone_kingco = LayerMapping(LSLD_Prone_kingco, LSLD_Prone_kingco_shp, LSLD_Prone_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_LSLD_Prone_kingco.save(strict=True, verbose=verbose)

    from .models import Volcano_Lahar_kingco
    lm_Volcano_Lahar_kingco = LayerMapping(Volcano_Lahar_kingco, Volcano_Lahar_kingco_shp, Volcano_Lahar_kingco_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Volcano_Lahar_kingco.save(strict=True, verbose=verbose)

# END OF GENERATED CODE BLOCK
######################################################

