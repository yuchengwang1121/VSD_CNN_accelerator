def init_parse(parser) :
    # modify the argument here
    parser.add_argument('--cpu', action='store_true',
                        help='set if only CPU is available')
    parser.add_argument('--data', action='store', default='./data/',
                        help='dataset path')
    parser.add_argument('--arch', action='store', default='nin',
                        help='the architecture for the network: nin')
    parser.add_argument('--opt', action='store', default='Adam',
                        help='the optimizer')
    parser.add_argument('--lr', action='store', default='0.1',
                        help='the intial learning rate')
    parser.add_argument('--pretrained', action='store', default=None,
                        help='the path to the pretrained model')
    parser.add_argument('--evaluate', action='store_true',
                        help='evaluate the model')
    parser.add_argument('--full', action='store', default='0',
                        help='full precision or not')
    parser.add_argument('--epoch', action='store', default='300',
                        help='training epoch')
    parser.add_argument('--write', action='store_true',
                        help='write_files')
    parser.add_argument('--predict', action='store_true',
                        help='predict single picture')
    return parser