from hash_set.multi_hash_set import MultiHashSet

if __name__ == '__main__':
    multi1 = MultiHashSet()
    multi1.add('1')
    multi1.add('2')
    multi1.add('3')
    multi1.add('4')
    multi1.add('5')
    multi1.add('6')
    multi1.add('7')
    multi1.add('8')
    multi1.add('9')
    multi1.add('10')
    multi1.add('11')
    multi1.add('12')
    multi1.add('13')
    multi1.add('14')
    multi1.add('15')



    print(str(multi1))
    print(multi1.contains('Krystian'))

    print('Krystian' in multi1)
