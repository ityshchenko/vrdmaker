import argparse
import jinja2 as j


def write_own_cfg(path, config):
    with open(path, 'w') as f:
        f.write(config)


def generate_settings(config: dict) -> str:
    env = j.Environment(loader=j.FileSystemLoader('templates'))
    template = env.get_template('default.xml')

    return template.render(ctx=config)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='My generator')

    parser.add_argument('-a', '--addr', help='address for "1C: Enterprise" server')
    parser.add_argument('-i', '--ibase', help='infobase name')
    parser.add_argument('-p','--pub', help='publication name')
    parser.add_argument('-d', '--debug', help='debug settings')
    parser.add_argument('-s', '--soap', help='list of soap service names')
    parser.add_argument('-hs', '--http', help='list of http service names')
    parser.add_argument('-o', '--output', help='output path')

    args = parser.parse_args()

    write_own_cfg(
        path=args.output,
        config=generate_settings(
            {
                'server_addr': args.addr,
                'ibase_name': args.ibase,
                'pub_name': args.pub,
                'debug': args.debug,
                'soap': args.soap.__str__().split(),
                'http': args.http.__str__().split(),
            }
        )
    )
    print(f'Config saved at {args.output}')
