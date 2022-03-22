server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_key, i_value in server_data.items():
    print("{k}:".format(
        k=i_key
    ))
    for j_key, j_value in i_value.items():
        print("{space}{k_2}: {v_2}".format(
            space=" " * 7,
            k_2=j_key,
            v_2=j_value
        ))
