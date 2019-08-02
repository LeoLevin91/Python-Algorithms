class QuickFindUF:
    # Этот класс реализует Алгоритм Быстрого поиска (QuickFind)
    # +Иницияализация весов
    # Добавление связей
    # +Идентификатор компоненты
    # +Определение связности
    # +Колличество компонент

    id = []
    # Колличество компонент
    count = 0

    def __init__(self, N):
        self.count = N
        for i in range(N):
            self.id.append(i)

    def find(self, p):
        # Возвращает идентификатор компоненты
        return self.id[p]

    def connection(self, p, q):
        # Определение связности
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)
        if (pID == qID): return

        for i in range(len(self.id)):
            if(self.id[i] == pID):
                self.id[i] = qID
        self.count = self.count - 1


    pass




if __name__ == '__main__':
    N = int(input("Введите колличество узлов: "))
    qS = QuickFindUF(N)
    while True:
         p = int(input("Узел A: "))
         q = int(input("Узел B: "))
         if (p == -1 or q == -1):
             break
         if(qS.connection(p, q)): continue
         qS.union(p, q)
         print(str(p) + " " + str(q))
    print(str(qS.count) + " компонентов.")

