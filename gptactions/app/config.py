import os

class Config:
    """Configuración base."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'una_llave_secreta_por_defecto')
    GOOGLE_SHEETS_CREDENTIALS_FILE = os.environ.get('GOOGLE_SHEETS_CREDENTIALS_FILE', 'ruta_por_defecto_a_credenciales.json')
    GOOGLE_SHEETS_SCOPE = ['https://spreadsheets.google.com/feeds',
                           'https://www.googleapis.com/auth/drive',
                           'https://www.googleapis.com/auth/spreadsheets']
    # Añade aquí otras configuraciones globales

class DevelopmentConfig(Config):
    """Configuraciones para desarrollo."""
    DEBUG = True
    # Otras configuraciones específicas de desarrollo

class ProductionConfig(Config):
    """Configuraciones para producción."""
    DEBUG = False
    # Asegúrate de que las credenciales y otros datos sensibles no sean accesibles o estén hardcodeados
    # Otras configuraciones específicas de producción
