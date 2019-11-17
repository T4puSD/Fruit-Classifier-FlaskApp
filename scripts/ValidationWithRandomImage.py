import tensorflow as tf,sys

def main(image_path):
    # image_path = sys.argv[1] if len(sys.argv)>=2 else 'abc.jpg'

    image_data = tf.gfile.FastGFile(image_path,'rb').read()
    label_lines = [line.rstrip() for line
                in tf.gfile.GFile('./scripts/training/data/retrained_labels.txt')]

    with tf.gfile.FastGFile('./scripts/training/data/retrained_graph.pb','rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def,name ='')

    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0':image_data})

        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        list1 = []
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            list1.append([human_string,score])
            print('%s (score = %.5f)' %(human_string,score))
        return list1


if __name__ == '__main__':
    image_path = sys.argv[1] if len(sys.argv)>=2 else 'abc.jpg'
    main(image_path)