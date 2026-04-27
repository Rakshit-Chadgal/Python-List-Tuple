#In this we have a list of grades acquired by a number of students. We will count the number of students with "A" grade, store the value in a list and sort them from "A" to "D"
G = ["C", "D", "A", "A", "B", "B", "A"]
G.sort()
print("Grades Sorted from A to D: ", G)

S = []
S.append(G.count("A"))
S.append(G.count("B"))
S.append(G.count("C"))
S.append(G.count("D"))
S.sort(reverse=True) #This will sort the list in descending order, so the highest count (for "A") will be first, followed by "B", "C", and "D".
print("Number of Students sorted by grade from A to D: ",S)