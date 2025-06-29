from flask import Flask, request, jsonify
from datetime import timedelta
from .extensions import db, jwt, ma, api, mi, cors, cloudinary
from .config import Config
from . import models



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["JWT_HEADER_TYPE"] = ""
    
    # Configurar duración del token JWT a 1 día
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

    # Debug: Verificar configuración cargada
    print("DB URI:", app.config.get('SQLALCHEMY_DATABASE_URI'))    # Inicializar extensiones
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    mi.init_app(app, db)
    api.init_app(app)
    cors.init_app(app)
    
    with app.app_context():
        # Crear todas las tablas si no existen
        db.create_all()
        
        # Verificar si las tablas específicas están vacías
        try:
            from .models.TipoEvaluacion_Model import TipoEvaluacion
            from .models.EvaluacionIntegral_Model import EvaluacionIntegral
            
            if TipoEvaluacion.query.count() == 0 and EvaluacionIntegral.query.count() == 0:
                # Solo ejecutar los seeders si ambas tablas están vacías
                from .seeds import run_seeders
                run_seeders()
            else:
                print("Las tablas ya contienen datos, no se requiere inicialización.")
        except Exception as e:
            print(f"Error al verificar las tablas: {e}")
            # Si hay error, intentar ejecutar los seeders
            try:
                from .seeds import run_seeders
                run_seeders()
            except Exception as seeder_error:
                print(f"Error al ejecutar seeders: {seeder_error}")
    
    # Elimina cualquier configuración previa  # Acceso directo a la configuración interna

    # Configuración directa y explícita
    cloudinary.config(
        cloud_name="dozywphod",
        api_key='441626374645742',
        api_secret='qJAFgRUbyHSVc_SitfIXj0ELXFI',
        secure=True
    )

    
    
    # Registrar Blueprints (rutas)
    from .routes.Estudiante_Routes import ns as estudiante_ns
    from .routes.Authentication_Routes import ns as authentication_ns
    from .routes.Docente_Routes import ns as docente_ns
    from .routes.Curso_Routes import ns as curso_ns
    from .routes.DocenteMateria_Routes import ns as docenteMateria_ns
    from .routes.Evaluacion_Routes import ns as evaluacion_ns
    from .routes.Gestion_Routes import ns as gestion_ns
    from .routes.Inscripcion_Routes import ns as inscripcion_ns
    from .routes.Materia_Routes import ns as materia_ns
    from .routes.MateriaCurso_Routes import ns as materiaCruso_ns
    from .routes.NotaEstimada_Routes import ns as notaEstimada_ns
    from .routes.NotaFinal_Routes import ns as notaFinal_ns
    from .routes.EvaluacionIntegral_Routes import ns as porcentaje_ns
    from .routes.TipoEvaluacion_Routes import ns as tipoEvaluacion_ns
    
    

    api.add_namespace(estudiante_ns)
    api.add_namespace(authentication_ns)
    api.add_namespace(docente_ns)
    api.add_namespace(curso_ns)
    api.add_namespace(docenteMateria_ns)
    api.add_namespace(evaluacion_ns)
    api.add_namespace(materia_ns)
    api.add_namespace(inscripcion_ns)
    api.add_namespace(materiaCruso_ns)
    api.add_namespace(notaEstimada_ns)
    api.add_namespace(notaFinal_ns)
    api.add_namespace(tipoEvaluacion_ns)
    api.add_namespace(porcentaje_ns)
    api.add_namespace(gestion_ns)
    
    
    return app