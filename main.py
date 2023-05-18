file_path = "data/NewsfeedPost"

if __name__ == '__main__':
    with open(file_path, 'r', encoding='utf-8') as f:
        all_data = f.read()
    print(all_data.count('"text":'))    # 95984
