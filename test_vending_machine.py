import unittest
import vendingMachine

class testVendingMachine(unittest.TestCase):

    def test_input(self):
        try:
            change=int(input("enter the change to be returned"))
            if change<=0:
                raise ValueError
        except ValueError:
            print("please enter a positive integer")
        else:
            notes=[1,2,5,10,50,100,500,1000]
            noOfNotes,notesUsed=vendingMachine.vendingMachine.getMinNotes(vendingMachine,change,notes)
            #noOfNotesTestCase,notesUsedTestCase,testMessage1,testMessage2=getTestInput(self)
            self.assertEqual(noOfNotes,7,"should be 7 for 237")
            self.assertEqual(notesUsed,[100, 100, 10, 10, 10, 5, 2],"should be this for 237")
            print("No. of notes: "+str(noOfNotes)+"\nNotes returned: "+str(notesUsed))

if __name__=='__main__':
    unittest.main()