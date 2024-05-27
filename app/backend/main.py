from services import Image_service

def main():
    user_service = Image_service()

    # Obtener avatares de usuarios
    avatars = user_service.get_user_avatars(page=2)
    print("Avatars:", avatars)

    # Obtener datos de un usuario específico
    user_data = user_service.get_single_user_data(2)
    print("Single User Data:", user_data)

    # Intentar obtener un usuario que no existe
    user_not_found = user_service.get_single_user_data(23)
    print("User Not Found:", user_not_found)

    # Obtener todos los recursos
    resources = user_service.get_all_resources()
    print("All Resources:", resources)

    # Obtener datos de un recurso específico
    resource_data = user_service.get_single_resource_data(2)
    print("Single Resource Data:", resource_data)

    # Intentar obtener un recurso que no existe
    resource_not_found = user_service.get_single_resource_data(23)
    print("Resource Not Found:", resource_not_found)

    # Crear un usuario
    new_user = user_service.create_user("morpheus", "leader")
    print("New User:", new_user)

    # Actualizar un usuario
    updated_user = user_service.update_user(2, "morpheus", "zion resident")
    print("Updated User:", updated_user)

    # Eliminar un usuario
    delete_status = user_service.delete_user(2)
    print("Delete User Status:", delete_status)

    # Registro exitoso
    register_success = user_service.register_user_successful("eve.holt@reqres.in", "pistol")
    print("Register Successful:", register_success)

    # Registro fallido
    register_fail = user_service.register_user_unsuccessful("sydney@fife")
    print("Register Unsuccessful:", register_fail)

    # Login exitoso
    login_success = user_service.login_user_successful("eve.holt@reqres.in", "cityslicka")
    print("Login Successful:", login_success)

    # Respuesta con retraso
    delayed_response = user_service.get_delayed_response(3)
    print("Delayed Response:", delayed_response)

if __name__ == "__main__":
    main()
