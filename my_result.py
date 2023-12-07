def check_attack_enemy(user_battle, key_crypt):
    from json import dumps, loads
    con = connect_to_db()
    cur = con.cursor()
    cur.execute(f'SELECT {user_battle["attack_coors_enemy"]} FROM {user_battle["hash"]}')
    coors_enemy = loads(cur.fetchone()[0])
    if coors_enemy:
        if user_battle['map_ship_cach'][coors_enemy["attack"][0]][coors_enemy["attack"][1]] == '#':
            user_battle['map_ship_cach'][coors_enemy["attack"][0]][coors_enemy["attack"][1]] = '%'
            user_battle['quant_point'] -= 1
            if user_battle['quant_point'] < 1:
                coors_enemy['status'] = 3
                con.close()            
                return True
            else:
                coors_enemy['status'] = 2
        else:
            coors_enemy['status'] = 1
            user_battle['map_ship_cach'][coors_enemy["attack"][0]][coors_enemy["attack"][1]] = '-'
        cur.execute(f'UPDATE {user_battle["hash"]} SET {user_battle["attack_coors_enemy"]} = {dumps(coors_enemy)}')
        cur.execute(f'UPDATE {user_battle["hash"]} SET {user_battle["map_ship"]} = aes_encrypt({dumps({"map_s":user_battle["map_ship_cach"]})}, {key_crypt})')
        con.commit()
    con.close()
    return False


