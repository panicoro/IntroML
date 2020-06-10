# Python script to transform to cvs

def get_csv():
    f = open('T8_3_FOOTBALL.DAT')
    data = f.read()

    lines = data.split('\n')

    csv_list = ['GR,WDIM,CIRCUM,FBEYE,EYEHD,HEARHD,JAW']
    for line in lines:
        sep = line.split(' ')
        split_spaces = line.split(' ')
        out_spaces = [word for word in split_spaces if word != '']    
        cline = ','.join(out_spaces)
        csv_list.append(cline)

    csv_data = '\n'.join(csv_list)
    filename = 'T8_3_FOOTBALL.csv'
    file_ = open(filename, 'w')
    file_.write(csv_data)
    file_.close()

def main():
    get_csv()

if __name__ == '__main__':
    main()
