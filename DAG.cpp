// Программа на C++ для вывода топологической сортировки DAG
 
#include<iostream>
#include <list>
#include <stack>
using namespace std;
  
// Класс для представления графа
class Graph
{
private:
    // Количество вершин
    int V;
  
    //  Указатель на массив, содержащий список смежности
    list<int> *adj;
  
    void topologicalSortUtil(int v, bool visited[], stack<int> &Stack)
    {
        // Помечаем текущий узел как посещенный
        visited[v] = true;
      
        // Рекурсивно вызываем функцию для всех смежных вершин
        list<int>::iterator i;
        for (i = adj[v].begin(); i != adj[v].end(); ++i)
            if (!visited[*i])
                topologicalSortUtil(*i, visited, Stack);
      
        // Добавляем текущую вершину в стек с результатом
        Stack.push(v);
    }

public:
    Graph(int V)   // Конструктор
    {
        this->V = V;
        adj = new list<int>[V];
    }
  
     // Функция для добавления ребра в граф
    void addEdge(int v, int w)
    {
        adj[v].push_back(w);
    }
  
    // Выводит топологическую сортировку графа
    void topologicalSort()
    {
        stack<int> Stack;
      
        // Помечаем все вершины как непосещенные
        bool *visited = new bool[V];
        for (int i = 0; i < V; i++)
            visited[i] = false;
      
        // Вызываем рекурсивную вспомогательную функцию 
        // для поиска топологической сортировки для каждой вершины
        for (int i = 0; i < V; i++)
          if (visited[i] == false)
            topologicalSortUtil(i, visited, Stack);
      
        // Выводим содержимое стека
        while (Stack.empty() == false)
        {
            cout << Stack.top() << " ";
            Stack.pop();
        }
    }
};

  
// Программа для тестирования 
int main()
{
    // Создаем граф, приведенный на диаграмме выше
    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    g.topologicalSort();
  
    return 0;
}
