import pbk
from args_man import parse_args
from bitcoin.core import CBlock

def main():
    args = parse_args()
    chain_man = pbk.load_chainman(args.datadir, args.chain_type)
    for block_index in pbk.block_index_generator(chain_man, start=args.start_height, end=args.end_height):
        block_data = chain_man.read_block_from_disk(block_index).data
        cblock = CBlock.deserialize(block_data)

if __name__ == '__main__':
    main()


