import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
def plot_confusion_matrix(cm,
                          target_names,
                          title='',
                          cmap=None,
                          normalize=True):
    """
    given a sklearn confusion matrix (cm), make a Nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name) # title of graph

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

    """
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    # plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.xlabel('Predicated label')
    plt.show()


# con = [[411,  12,  10,  66,   1],
#         [ 32, 436,   3,   8,  21],
#         [113,  60,  45,  10,   0],
#         [270,   2 ,  1, 227,   0],
#         [  1,  35,   2,   1, 461]]
# # ax= plt.subplot()
# # sn.heatmap(con, annot=False, cmap='Purples', ax=ax)
# label = ['Answerable', 'Improper', 'Ambiguous', 'ExtKnow',
#           'Non-SQL']

con = [
        [ 436,   8,    3,   21,  32,],
        [   2,   227,  1,   0,   270,],
        [  60,   10,  45,   0,   113,],
        [  35,   1,   2,   461,    1,],
        [  12,   66,  10,   1,   411,]
      ]
# ax= plt.subplot()
# sn.heatmap(con, annot=False, cmap='Purples', ax=ax)
label = [ 'Improper','ExtKnow', 'Ambiguous', 'Non-SQL',
          'Answerable']

# ax.xaxis.set_ticklabels(label)
# ax.yaxis.set_ticklabels(label)
# plt.show()
plot_confusion_matrix(np.array(con), label, normalize=False)