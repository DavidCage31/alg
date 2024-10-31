using System;
using System.Numerics;
using System.IO;

namespace laba
{
    class Program
    {
        public class GraphNode
        {
            public List<GraphNode> LinkedNodes;
            public int Tag;

            public GraphNode()
            {
                this.LinkedNodes = new List<GraphNode>();
                this.Tag = 0;
            }
        }

        public class Graph
        {
            public List<GraphNode> nodes;

            public Graph()
            {
                this.nodes = new List<GraphNode>();
            }

            public void TopologicSort()
            {
                List<List<GraphNode>> levels = new List<List<GraphNode>>();
                int?[] workArray = GetInputNodesArray();
                int completedCounter = 0;
                int currentLevel = 0;

                while (completedCounter != this.nodes.Count)
                {
                    levels.Add(new List<GraphNode>());

                    // Во избежание обработки вершин, с нулевой
                    // степенью захода, возникших по ходу следующего цикла,
                    // помечаем их заранее.

                    for (int i = 0; i < this.nodes.Count; i++)
                        if (workArray[i] == 0)
                            workArray[i] = null;

                    for (int i = 0; i < this.nodes.Count; i++)
                    {
                        if (workArray[i] == null)
                        {
                            // Если вершину следует обработать, помещаем её
                            // В соответствующий ей уровень и корректируем
                            // Массив степеней захода остальных вершин

                            levels[currentLevel].Add(this.nodes[i]);

                            this.nodes[i].Tag = currentLevel; // Оставляем в вершине метку о её уровне

                            foreach (GraphNode node in this.nodes[i].LinkedNodes)
                            {
                                int linkedNode = this.nodes.IndexOf(node);

                                workArray[linkedNode]--;
                            }

                            workArray[i] = -1; // Помечаем вершину как обработанную

                            completedCounter++;
                        }
                    }

                    currentLevel++;
                }
            }

            int?[] GetInputNodesArray()
            {
                int?[] array = new int?[this.nodes.Count];

                for (int i = 0; i < this.nodes.Count; i++)
                    array[i] = this.nodes[i].LinkedNodes.Count;

                return array;
            }
        }

        static void Main(string[] args) 
        {
            
        }
    }
}