def read_file_to_dict(filename):
    file_path = filename
    objective_dict = dict()
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            product_split = content.split(';')
            for sell in product_split:
                sell_split = sell.split(":")
                sell_name = sell_split[0]
                try:
                    sell_value = float(sell_split[1])
                except IndexError:
                    print(f"Error: El formato de la línea '{sell}' es incorrecto.")
                    continue
                except ValueError:
                    print(f"Error al convertir el valor de {sell_name}")
                    continue
                if sell_name not in objective_dict:
                    objective_dict[sell_name] = [sell_value]
                else:
                    objective_dict[sell_name].append(sell_value)
        return objective_dict
    except FileNotFoundError:
        print("Archivo no encontrado")
        raise

def process_dict(objective_dict):
    new_obj_dict = dict()
    for sell_name, sells_values in objective_dict.items():
        total_sells = sum(sells_values)
        average_sells = total_sells / len(sells_values)
        print(f"{sell_name}: ventas totales ${total_sells:.2f}, promedio ${average_sells:.2f}")    
