def init_parse(parser) :        # modify the argument here
    # The core type to run model
    parser.add_argument('--cpu', action='store_true',
                        help='set if only CPU is available')
    # Choose the Model structure
    parser.add_argument('--arch', action='store', default='nin',
                        help='the architecture for the network: nin')
    # Choose the type of optimizer
    parser.add_argument('--opt', action='store', default='Adam',
                        help='the optimizer')
    # learning rate for optimizer
    parser.add_argument('--lr', action='store', default='0.001',
                        help='the intial learning rate')
    # load trained model's dict
    parser.add_argument('--pretrained', action='store', default=None,
                        help='the path to the pretrained model')
    # full precision for Conv2d
    parser.add_argument('--full', action='store', default='0',
                        help='full precision or not')
    # Total epoch the model train & validate
    parser.add_argument('--epoch', action='store', default='30',
                        help='training epoch')
    # write the model's parameter into .HEX file
    parser.add_argument('--write', action='store_true',
                        help='write_files')
    # Validating model
    parser.add_argument('--evaluate', action='store_true',
                        help='evaluate the model')
    # Testing the data
    parser.add_argument('--predict', action='store_true',
                        help='predict single picture')
    return parser