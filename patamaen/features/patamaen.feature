Feature: 書寫規範
句首大寫、豆號後空白

Scenario Outline: 句首大寫.
   When Mitilid ko tamdaw <tilid>
   Then 改 to <matamaay>
   
   Examples: 句首大寫，Ano 遇到 to 大寫，改 to 小寫
   | tilid      | matamaay   |
   | nga'ay ho? | Nga'ay ho? |
   
   Examples: 豆號後空白
   | tilid                    | matamaay                  |
   | Ci Panay kako,nga'ay ho? | Ci Panay kako, nga'ay ho? |
   
   Examples: 豆號前bē-sái空白
   | tilid                     | matamaay                  |
   | Ci Panay kako ,nga'ay ho? | Ci Panay kako, nga'ay ho? |