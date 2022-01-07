from cursor_del_pool import CursorDelPool

class PersonaDAO:
    _insertar = 'INSERT INTO persona(id_empresa, nombre, telefono_fijo, telefono_celular, mail, tipo_relacion, observaciones) VALUES(%s, %s, %s, %s, %s, %s, %s)'
    _seleccionar = 'SELECT * FROM persona'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = []
                for i in range(8):
                    persona.append(registro[i])
                personas.append(persona)
            return personas

    @classmethod
    def seleccionar_uno(cls, valores):
        with CursorDelPool() as cursor:
            query = f'{cls._seleccionar_uno} {valores[0]} = \'{valores[1]}\''
            cursor.execute(query)
            registros = cursor.fetchall()
            if cursor.rowcount != 1:
                personas = []
                for registro in registros:
                    persona = []
                    for i in range(8):
                        persona.append(registro[i])
                    personas.append(persona)
            else:
                personas = list(registros)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            if type(persona) == dict:
                valores = []
                for clave in persona:
                    valores.append(persona[clave])
            elif type(persona) == list:
                valores = persona
            valores = tuple(valores)
            cursor.execute(cls._insertar, valores)

if __name__ == '__main__':
    print(PersonaDAO.ultimo())