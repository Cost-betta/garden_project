from enumchoicefield import ChoiceEnum
from django.utils.translation import gettext_lazy as _


class ColorLeafType(ChoiceEnum):
    """Возможная окраска листьев"""

    GREEN = _('Green')
    RED = _('Red')
    UNKNOWN = _('Unknown')


class ShapeNutType(ChoiceEnum):
    """Возможная форма ореха"""

    CIRCLE = _('Circle')
    CONE = _('Cone')
    CYLINDER = _('Cylinder')
    UNKNOWN = _('Unknown')
    OVAL = _('Oval')


class RegionType(ChoiceEnum):
    """Регионы произрастания"""

    SPANISH_ITALIAN = _('Spanish-Italian'),
    CENTRAL_EUROPEAN = _('Central European')
    ENGLISH = _('English')
    BLACK_SEA = _('Black Sea')
    OTHER = _('Other')
    OSU = _('OSU')
    OSUS = _('OSUs')
    INTERSPECIFIC_HYBRID = _('Interspecific hybrids')
    UNKNOWN = _('Unknown')


class CountryType(ChoiceEnum):
    """Возможные страны происхождения"""

    ALBANIA = _('Albania')
    ARGENTINA = _('Argentina')
    AUSTRALIA = _('Australia')
    AZERBAIJAN = _('Azerbaijan')
    BULGARIA = _('Bulgaria')
    CANADA = _('Canada')
    CHILE = _('Chile')
    CHINA = _('China')
    DENMARK = _('Denmark')
    ESTONIA = _('Estonia')
    FINLAND = _('Finland')
    FRANCE = _('France')
    GEORGIA = _('Georgia')
    GERMANY = _('Germany')
    GERMANY_POLAND = _('Germany/Poland')
    GREECE = _('Greece')
    GREECE_TURKEY = _('Greece/Turkey')
    ITALY = _('Italy')
    MACEDONIA = _('Macedonia')
    NETHERLANDS_GERMANY = _('Netherlands/Germany')
    NEW_ZEALAND = _('New Zealand')
    POLAND = _('Poland')
    PORTUGAL = _('Portugal')
    ROMANIA = _('Romania')
    RUSSIA = _('Russia')
    RSFSR = _('RSFSR')
    SERBIA = _('Serbia')
    SERBIA_SLOVENIA = _('Serbia(Slovenia)')
    SLOVENIA = _('Slovenia')
    SOUTHERN_EUROPE = _('Southern Europe')
    SPAIN = _('Spain')
    TURKEY = _('Turkey')
    UKRAINE = _('Ukraine')
    UKRAINIAN_SSR = _('Ukrainian SSR')
    UNITED_KINGDOM = _('United Kingdom')
    USA = _('USA')
    UNKNOWN = _('Unknown')
