import os
import argparse

def define_argparser():
    parser = argparse.ArgumentParser(description='Analyzer for word & sentence count')

    # input file name
    parser.add_argument('--load-file', '-lf',  required=True, help='file name of the data')

    # analyzer option
    parser.add_argument(
        '--process-option', '-po',
        default='a',
        help='w: count words, s: count sentences, a: count words & sentences'
    )

    # output option
    parser.add_argument(
        '--result-file', '-rf',
        default=False,
        help='the file name for result'
    )

    return parser.parse_args()

def main(config):
    with open(config.load_file, 'rt', encoding='utf-8') as f:
        data = f.readlines()
    
    # Count the number of sentences
    data = [x for x in data if x !='\n']
    num_sentences = len(data)
    
    num_words = 0
    for line in data:
        line = line.split(' ')
        num_words += len(line)
    
    if config.process_option == 'w':
        print('Word count:{}'.format(num_words))
        print()
    elif config.process_option == 's':
        print('Sentence count: {}'.format(num_sentences))
        print()
    else:
        print('Word count:{}'.format(num_words))
        print('Sentence count: {}'.format(num_sentences))
        print()
    
    if config.result_file:
        with open(config.result_file, 'wt', encoding='utf-8') as f:
            f.write('Wrod count: {}\n'.format(num_words))
            f.write('Sentence count: {}\n'.format(num_sentences))
    
if __name__=='__main__':
    config = define_argparser()
    main(config)
