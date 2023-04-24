import ruamel.yaml as yaml
import json


if __name__=="__main__":
    print("Làm việc với file Yaml")
    with open ("user.yaml","r") as stream:
        user_yaml= yaml.safe_load(stream)

    print("Type of user_yaml variable:")
    print(type(user_yaml))
    print('----------------------')
    print("Print Key:")
    for key in user_yaml:
        print(key)
    print('----------------------')

    print("ID:",user_yaml["id"])
    print("First name:",user_yaml["first_name"])
    print("------------------")
    print("Key of address:")
    print(user_yaml['address'])

    adr=user_yaml["address"][0]
    print(adr)
    print(adr["city"])
    print('----------------------')
    # for i in range(0,len(user_yaml["address"])):

    #     print(user_yaml["address"][i]['city'])


    print('----------------------')
    user__json=json.dumps(user_yaml, default=str , indent=4, sort_keys=True)
    print(user__json)
    file=open("user.json","w")
    file.write(user__json)
    file.close()
    # Iterate over the keys of the user_yaml and print them
    # print('Keys in user_yaml:')
    # for key in user_yaml:
    #     print(key)
    # print('----------------------')
    # # Create JSON structre with indents and soreted keys
    # print('JSON with indents and sorted keys')
    # user_json = json.dumps(user, default=str, indent=4, sort_keys=True)
    # print(user_json)
    # print('----------------------')
    # # Print to file user.json
    # file = open("user.json","w")
    # file.write(user_json)
    # file.close()