import click

'''click 是使用装饰器的方式给函数添加命令行属性'''
@click.command()
@click.option('--name',default='Leijun',help='name 参数，非必须，有默认值')
@click.option('--year',help='year 参数',type=int)
@click.option('--body',help='body 参数')
def test_for_sys(year, name, body):
    print('the year is', year)
    print('the name is', name)
    print('the body is', body)

if __name__ == '__main__':
    test_for_sys()

'''
比较特殊的是最后调用函数的时候是没有带上参数的，因为参数会自动通过命令行的形式传入。其他设置参数的属性跟前面的 argparse 的方式非常相似，
'''