import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables de .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://escuela_8lcq_user:kpuXPA7k4xYFmTNQqBIeW8tQmg1wgzBc@dpg-d0uqvbeuk2gs739bo2ng-a.oregon-postgres.render.com/escuela_8lcq'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Nuevas configuraciones para Cloudinary
    CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')

    