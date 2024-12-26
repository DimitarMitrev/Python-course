#najdi_samoglaski = [bukva for bukva in zbor if bukva in samoglaski and bukva not in najdi_samoglaski]
zbor = input("Vnesi zbor: ")
samoglaski = ["a",'e','i','o','u']
samoglaski_vo_zbor = [[bukva for bukva in zbor if bukva in samoglaski and bukva not in samoglaski]:
print(samoglaski_vo_zbor)