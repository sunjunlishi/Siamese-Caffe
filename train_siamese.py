import os
caffe_root = os.environ['CAFFE_DIR']
import sys
sys.path.append(caffe_root +  '/python')

import caffe
import siamese_krayni

caffe.set_device(0)
caffe.set_mode_gpu()

solver = caffe.SGDSolver('solver_siamse.prototxt')
solver.solve()

