def persinfo_func(name: str, surname: str, dob: str, city: str, email: str, phone: str):
    data_dict = [name, surname, dob, city, email, phone]
    s = ', '
    print(s.join(data_dict))
    print(type(s.join(data_dict)))
    return data_dict

persinfo_func('David', 'Markov', '18/12/56', 'Moskow', 'david@moscow.com', '+19439439394')
