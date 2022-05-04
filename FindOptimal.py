from bisect import insort


class FindOptimal:

    def __init__(self, groups, heuristics, evaluate_fnc):
        self.groups = groups
        self.heuristics = heuristics
        self.evaluate_fnc = evaluate_fnc
        self.count = 0


    def find_optimal(self, selection, explored, min_selected, amount_selected):
        self.count += 1
        score = self.evaluate_fnc(selection)
        selections = [(score, selection.copy())]
        explored['_'.join(selection)] = score

        for element in selection:
            self.remove_element(element, selection)
            if not self.heuristics_triggered(selection, explored, min_selected, amount_selected-1):
                selections.append(self.find_optimal(selection, explored, min_selected, amount_selected-1))
            self.insert_element(element, selection)

        selections.sort(reverse=True)
        return selections[0]


    def remove_element(self, element, selection):
        if element in self.groups:
            for e in self.groups.get(element):
                selection.remove(e)
        selection.remove(element)


    def insert_element(self, element, selection):
        if element in self.groups:
            for e in self.groups.get(element):
                insort(selection, e)
        insort(selection, element)


    def heuristics_triggered(self, selection, explored, min_selected, amount_selected):
        if '_'.join(selection) in explored:
            return True
        if amount_selected < min_selected:
            return True
        return False
