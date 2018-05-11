class wadjList:
    def __init__(self,words):
        self.wMap = {
            'cat' = ['rat','hat','bat','cut','cap','can','car'],
            'car' = ['tar','far']
            'hat' = ['ham']
        }

    #'cat' to 'ham'

    #make the queue
    # insert cat and make it visited with parent being None
    # Dequeue cat and go to each neighr and enqueue if it is not
    # found in the visited list
    # Keep dequeing and if the current_word is target word return with
    # the visitedlist and compute the back-ref.

