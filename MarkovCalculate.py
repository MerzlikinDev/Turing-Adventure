import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import time
import threading

class MarkovMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Машина Маркова")
        self.root.geometry("800x600")
        
        self.rules = {}
        self.running = False
        self.current_theme = "light"
        
        self.light_theme = {
            'bg': '#f0f0f0',
            'fg': '#000000',
            'entry_bg': '#ffffff',
            'entry_fg': '#000000',
            'button_bg': '#e1e1e1',
            'button_fg': '#000000',
            'tree_bg': '#ffffff',
            'tree_fg': '#000000',
            'text_bg': '#ffffff',
            'text_fg': '#000000',
            'select_bg': '#0078d7',
            'select_fg': '#ffffff'
        }
        
        self.dark_theme = {
            'bg': '#2d2d2d',
            'fg': '#ffffff',
            'entry_bg': '#3d3d3d',
            'entry_fg': '#ffffff',
            'button_bg': '#3d3d3d',
            'button_fg': '#ffffff',
            'tree_bg': '#3d3d3d',
            'tree_fg': '#ffffff',
            'text_bg': '#3d3d3d',
            'text_fg': '#ffffff',
            'select_bg': '#0078d7',
            'select_fg': '#ffffff'
        }
        
        self.create_widgets()
        self.apply_theme()
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        theme_frame = ttk.Frame(main_frame)
        theme_frame.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=5)
        
        ttk.Label(theme_frame, text="Тема:").grid(row=0, column=0, padx=5)
        self.theme_var = tk.StringVar(value="Светлая")
        theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var, values=["Светлая", "Темная"], state="readonly", width=10)
        theme_combo.grid(row=0, column=1, padx=5)
        theme_combo.bind('<<ComboboxSelected>>', self.change_theme)
        
        ttk.Label(main_frame, text="Входное слово:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.word_entry = ttk.Entry(main_frame, width=50)
        self.word_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(main_frame, text="Правила подстановки:").grid(row=2, column=0, sticky=tk.W, pady=5)
        
        rules_frame = ttk.Frame(main_frame)
        rules_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        columns = ('Левая часть', 'Правая часть', 'Тип')
        self.rules_tree = ttk.Treeview(rules_frame, columns=columns, show='headings', height=8)
        
        for col in columns:
            self.rules_tree.heading(col, text=col)
            self.rules_tree.column(col, width=150)
        
        rules_scrollbar = ttk.Scrollbar(rules_frame, orient=tk.VERTICAL, command=self.rules_tree.yview)
        self.rules_tree.configure(yscrollcommand=rules_scrollbar.set)
        
        self.rules_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        rules_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(input_frame, text="Левая часть:").grid(row=0, column=0, padx=5)
        self.left_entry = ttk.Entry(input_frame, width=15)
        self.left_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(input_frame, text="Правая часть:").grid(row=0, column=2, padx=5)
        self.right_entry = ttk.Entry(input_frame, width=15)
        self.right_entry.grid(row=0, column=3, padx=5)
        
        self.rule_type = tk.StringVar(value="->")
        ttk.Radiobutton(input_frame, text="Обычное (->)", variable=self.rule_type, value="->").grid(row=0, column=4, padx=5)
        ttk.Radiobutton(input_frame, text="Заключительное (=>)", variable=self.rule_type, value="=>").grid(row=0, column=5, padx=5)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="Добавить правило", command=self.add_rule).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Удалить правило", command=self.delete_rule).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Очистить правила", command=self.clear_rules).grid(row=0, column=2, padx=5)
        
        execute_frame = ttk.Frame(main_frame)
        execute_frame.grid(row=6, column=0, columnspan=3, pady=10)
        
        self.execute_btn = ttk.Button(execute_frame, text="Выполнить", command=self.execute_markov)
        self.execute_btn.grid(row=0, column=0, padx=5)
        
        self.stop_btn = ttk.Button(execute_frame, text="Остановить", command=self.stop_execution, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=5)
        
        ttk.Button(execute_frame, text="Очистить результат", command=self.clear_output).grid(row=0, column=2, padx=5)
        
        ttk.Label(main_frame, text="Результат:").grid(row=7, column=0, sticky=tk.W, pady=5)
        
        self.output_text = scrolledtext.ScrolledText(main_frame, width=70, height=10, wrap=tk.WORD)
        self.output_text.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        main_frame.rowconfigure(8, weight=1)
        rules_frame.columnconfigure(0, weight=1)
        rules_frame.rowconfigure(0, weight=1)
        
    def apply_theme(self):
        theme = self.dark_theme if self.current_theme == "dark" else self.light_theme
        
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('.', background=theme['bg'], foreground=theme['fg'])
        style.configure('TLabel', background=theme['bg'], foreground=theme['fg'])
        style.configure('TFrame', background=theme['bg'])
        style.configure('TButton', background=theme['button_bg'], foreground=theme['button_fg'])
        style.map('TButton', background=[('active', theme['select_bg'])])
        style.configure('TEntry', fieldbackground=theme['entry_bg'], foreground=theme['entry_fg'])
        style.configure('TCombobox', fieldbackground=theme['entry_bg'], foreground=theme['entry_fg'])
        style.configure('TRadiobutton', background=theme['bg'], foreground=theme['fg'])
        
        style.configure('Treeview', background=theme['tree_bg'], foreground=theme['tree_fg'], fieldbackground=theme['tree_bg'])
        style.map('Treeview', background=[('selected', theme['select_bg'])], foreground=[('selected', theme['select_fg'])])
        
        self.root.configure(bg=theme['bg'])
        self.output_text.configure(bg=theme['text_bg'], fg=theme['text_fg'], insertbackground=theme['fg'])
        
    def change_theme(self, event=None):
        self.current_theme = "dark" if self.theme_var.get() == "Темная" else "light"
        self.apply_theme()
        
    def add_rule(self):
        left = self.left_entry.get().strip()
        right = self.right_entry.get().strip()
        rule_type = self.rule_type.get()
        
        if not left or not right:
            messagebox.showwarning("Предупреждение", "Заполните оба поля!")
            return
        
        self.rules[left] = [right, rule_type]
        self.rules_tree.insert('', tk.END, values=(left, right, rule_type))
        
        self.left_entry.delete(0, tk.END)
        self.right_entry.delete(0, tk.END)
        
    def delete_rule(self):
        selected = self.rules_tree.selection()
        if selected:
            item = self.rules_tree.item(selected[0])
            left = item['values'][0]
            
            if left in self.rules:
                del self.rules[left]
            
            self.rules_tree.delete(selected[0])
    
    def clear_rules(self):
        self.rules.clear()
        for item in self.rules_tree.get_children():
            self.rules_tree.delete(item)
    
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
    
    def check_cycle(self):
        for key in self.rules:
            d = self.rules[key][0]
            if d in self.rules:
                if (self.rules[d][0] == key) and (self.rules[d][1] == self.rules[key][1]):
                    return True
        return False
    
    def markovs_machine(self, word):
        if self.check_cycle():
            return "цикл (обнаружен в правилах)"
        
        sm_fd = True
        steps = 0
        max_steps = 1000
        
        while sm_fd and self.running:
            count = 0
            
            for i in self.rules.keys():
                if i not in word:
                    count += 1
                    if count == len(list(self.rules.keys())):
                        sm_fd = False
                        return word
                else:
                    break
            
            if not sm_fd:
                break
            
            time1 = time.time()
            
            for i in list(self.rules.keys()):
                if not self.running:
                    return "Прервано пользователем"
                
                if self.rules[i][1] == "->":
                    while i in word and self.running:
                        word = word.replace(i, self.rules[i][0], 1)
                        steps += 1
                        
                        self.root.after(0, self.update_output, word, steps)
                        
                        time_dis = time.time() - time1
                        if time_dis > 7.5:
                            return "цикл (превышено время выполнения)"
                        
                        if steps > max_steps:
                            return "цикл (превышено количество шагов)"
                            
                elif self.rules[i][1] == "=>":
                    if i in word:
                        word = word.replace(i, self.rules[i][0], 1)
                        self.root.after(0, self.update_output, word, steps)
                        return word
            
            self.root.after(0, self.update_output, word, steps)
        
        return word
    
    def update_output(self, word, steps):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Шаг {steps}: {word}\n")
        self.output_text.see(tk.END)
    
    def execute_markov(self):
        word = self.word_entry.get().strip()
        
        if not word:
            messagebox.showwarning("Предупреждение", "Введите входное слово!")
            return
        
        if not self.rules:
            messagebox.showwarning("Предупреждение", "Добавьте хотя бы одно правило!")
            return
        
        self.execute_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.running = True
        
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Начальное слово: {word}\n")
        self.output_text.insert(tk.END, "Применяемые правила:\n")
        
        thread = threading.Thread(target=self.run_markov, args=(word,))
        thread.daemon = True
        thread.start()
    
    def run_markov(self, word):
        result = self.markovs_machine(word)
        self.root.after(0, self.execution_finished, result)
    
    def execution_finished(self, result):
        self.output_text.insert(tk.END, f"\nРезультат: {result}")
        self.execute_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.running = False
    
    def stop_execution(self):
        self.running = False
        self.output_text.insert(tk.END, "\nВыполнение остановлено пользователем")

def main():
    root = tk.Tk()
    app = MarkovMachineGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
