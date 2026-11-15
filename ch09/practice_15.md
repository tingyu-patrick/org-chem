# Ch09 Alkynes 精選 15 題練習清單（重質不重量・含命名與隱藏詳解）

> 對應課本檔案：[ch09.pdf](ch09.pdf)（McMurry *Organic Chemistry* Ch.9, pp. 284–286l）  
> 對應筆記索引：[index.md](index.md)

---

## 第一部分：IUPAC 命名與結構基礎（2 題）

### - [ ] 1. Problem 9-26 (p. 286e) ⭐⭐ 【IUPAC 命名核心規則與陷阱】
**題目重點**：為課本 p. 286e 的 6 個炔類／烯炔分子進行 IUPAC 命名（特別注意 **(c)** 與 **(e)** 雙鍵 vs. 叁鍵的編號優先權，以及 **(f)** 對稱叁鍵的取代基編號陷阱！）：
- (a) $\text{CH}_3\text{CH}_2\text{C}\equiv\text{CC(CH}_3)_3$
- (b) $\text{CH}_3\text{C}\equiv\text{CCH}_2\text{C}\equiv\text{CCH}_2\text{CH}_3$
- (c) $\text{CH}_3\text{CH=C(CH}_3)\text{C}\equiv\text{CCH(CH}_3)_2$
- (d) $\text{HC}\equiv\text{CC(CH}_3)_2\text{CH}_2\text{C}\equiv\text{CH}$
- (e) $\text{H}_2\text{C=CHCH=CHC}\equiv\text{CH}$
- (f) $\text{CH}_3\text{CH}_2\text{CH(CH}_2\text{CH}_3)\text{C}\equiv\text{CCH(CH}_2\text{CH}_3)\text{CH(CH}_3)_2$

<details>
<summary>💡 點擊展開答案與詳解</summary>

**炔類與烯炔（Enynes）IUPAC 命名三大法則**：
1. 優先選擇包含所有雙鍵與叁鍵的最長碳鏈為主鏈。
2. 從距離多重鍵（不論是雙鍵或叁鍵）較近的一端開始編號，使多重鍵獲得最小位次組合。
3. **平手決勝原則**：若從兩端編號時，多重鍵的位次組合完全相同，則**雙鍵（-en-）優先獲得較小數字**（字尾永遠寫成 `-en-yne`，拿掉 -ene 字尾的 e）。

- **(a) 2,2-Dimethyl-3-hexyne**
  - **解析**：最長鏈 6 碳；從右端編號使叁鍵在 C3（若從左端則在 C3，但右端可同時讓兩個甲基在 C2：右起叁鍵 C3、甲基 `2,2` vs. 左起叁鍵 C3、甲基 `5,5`，故從右端編號）。
- **(b) 2,5-Octadiyne**
  - **解析**：8 碳二炔，從左端編號得 `2,5-`，比從右端的 `3,6-` 更小。
- **(c) 3,6-Dimethyl-2-hepten-4-yne**
  - **解析**：主鏈 7 碳。比較兩端的多重鍵位置：從左端起算為 C2（雙鍵）與 C4（叁鍵）$\rightarrow$ `(2,4)`；從右端起算為 C3（叁鍵）與 C5（雙鍵）$\rightarrow$ `(3,5)`。因為 `(2,4) < (3,5)`，由左向右編號！
- **(d) 3,3-Dimethyl-1,5-hexadiyne**
  - **解析**：兩端皆為末端叁鍵 `(1,5)` 平手，故從左端編號讓兩個甲基位於 C3（`3,3` $<$ `4,4`）。
- **(e) 1,3-Hexadien-5-yne**
  - **解析**：**經典平手題**！從左端編號多重鍵位於 `(1,3,5)`；從右端編號多重鍵也位於 `(1,3,5)`。多重鍵位次完全平手時，**雙鍵優先拿 C1**，故從左端 $\text{H}_2\text{C=CH}-$ 開始編號！
- **(f) 3,6-Diethyl-2-methyl-4-octyne**
  - **解析**：**最常錯的陷阱題**！包含叁鍵的最長主鏈為 8 個碳（octyne），無論從左端或右端算，叁鍵都剛好在第 4 號碳（`4-octyne`）。此時必須比較**取代基位次組合**：
    - 若從左端算：取代基在 `(3,6,7)`；
    - 若從右端（含異丙基那端）算：C1 為甲基、C2 接甲基、C3 接乙基、C6 接乙基，取代基位次為 **`(2,3,6)`**！
    - 因為 `(2,3,6) < (3,6,7)`，必須從右端編號，得 `3,6-diethyl-2-methyl-4-octyne`！
</details>

---

### - [ ] 2. Problem 9-27 & 9-17 (pp. 286e, 286b) ⭐ 【由名稱畫結構＆環炔張力】
**題目重點**：
1. 畫出 **9-27** 下列名稱對應的結構（挑最具代表性的 4 個）：
   - (b) `3-Ethyl-5-methyl-1,6,8-decatriyne`
   - (d) `3,4-Dimethylcyclodecyne`
   - (f) `3-Chloro-4,4-dimethyl-1-nonen-6-yne`
   - (h) `5-tert-Butyl-2-methyl-3-octyne`
2. **結合 9-17 (p. 286b)**：為什麼 9-27(d) 的十元環炔 `cyclodecyne` 可以穩定存在，而 9-17 的五元環炔 `cyclopentyne` 卻極度不穩定無法存在？

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **結構式要點**：
   - **(b) `3-Ethyl-5-methyl-1,6,8-decatriyne`**：10 碳主鏈，在 C1≡C2、C6≡C7、C8≡C9 畫三個叁鍵，C3 接 $-\text{CH}_2\text{CH}_3$，C5 接 $-\text{CH}_3$：
     $$\text{HC}\equiv\text{C}-\text{CH(C}_2\text{H}_5)-\text{CH}_2-\text{CH(CH}_3)-\text{C}\equiv\text{C}-\text{C}\equiv\text{C}-\text{CH}_3$$
   - **(d) `3,4-Dimethylcyclodecyne`**：10 元環內C1≡C2 為叁鍵，緊鄰的 C3 與 C4 各接一個 $-\text{CH}_3$。
   - **(f) `3-Chloro-4,4-dimethyl-1-nonen-6-yne`**：9 碳主鏈，C1=C2 為雙鍵，C6≡C7 為叁鍵，C3 接 $-\text{Cl}$，C4 接兩個 $-\text{CH}_3$：
     $$\text{H}_2\text{C=CH}-\text{CH(Cl)}-\text{C(CH}_3)_2-\text{CH}_2-\text{C}\equiv\text{C}-\text{CH}_2\text{CH}_3$$
   - **(h) `5-tert-Butyl-2-methyl-3-octyne`**：8 碳主鏈，C3≡C4 為叁鍵，C2 接 $-\text{CH}_3$，C5 接 $-\text{C(CH}_3)_3$：
     $$(\text{CH}_3)_2\text{CH}-\text{C}\equiv\text{C}-\text{CH[C(CH}_3)_3]\text{CH}_2\text{CH}_2\text{CH}_3$$
2. **9-17 環炔張力解析**：
   - 叁鍵碳為 **$sp$ 混成**，理想鍵角為 **$180^\circ$（直線形）**，即 $\text{C}-\text{C}\equiv\text{C}-\text{C}$ 四個碳原子必須共線。
   - 五元環（`cyclopentyne`）太小，強行將 $180^\circ$ 的四碳直線段折彎成五邊形會產生毀滅性的**角張力（angle strain）**；而十元環（`cyclodecyne`）有足夠的 $-\text{CH}_2-$ 鏈長可以輕鬆容納直線形的 $\text{C}-\text{C}\equiv\text{C}-\text{C}$ 單元而無明顯張力。
</details>

---

## 第二部分：核心反應、水合與立體選擇性（3 題）

### - [ ] 3. Problem 9-31 & 9-33 (p. 286f) ⭐⭐ 【末端炔 vs. 不對稱內部炔反應全對照】
**題目重點**：比較**末端炔 `1-hexyne`**（9-31）與**不對稱內部炔 `2-hexyne`**（9-33）在各核心試劑下的產物差異：
- **Part A (`1-hexyne`)**：(a) 1 equiv $\text{HBr}$、(b) 1 equiv $\text{Cl}_2$、(d) $\text{NaNH}_2/\text{NH}_3$ then $\text{CH}_3\text{Br}$、(e) $\text{H}_2\text{O}, \text{H}_2\text{SO}_4, \text{HgSO}_4$、(f) 2 equiv $\text{HCl}$
- **Part B (`2-hexyne`)**：(b) 1 equiv $\text{HBr}$、(d) $\text{Li}$ in $\text{NH}_3$、(e) $\text{H}_2\text{O}, \text{H}_2\text{SO}_4, \text{HgSO}_4$

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **Part A：末端炔 `1-hexyne`（區域選擇性極佳，皆得單一位置異構物）**
  - **(a) 1 equiv $\text{HBr}$** $\rightarrow$ **2-bromo-1-hexene**（Markovnikov，$-\text{Br}$ 接內部碳 C2）。
  - **(b) 1 equiv $\text{Cl}_2$** $\rightarrow$ **(E)-1,2-dichloro-1-hexene**（*anti* 加成，兩 $-\text{Cl}$ 互為 *trans*）。
  - **(d) $\text{NaNH}_2$ then $\text{CH}_3\text{Br}$** $\rightarrow$ **2-heptyne**（乙炔負離子 $\text{S}_\text{N}2$ 烷基化）。
  - **(e) $\text{H}_2\text{O}, \text{H}_2\text{SO}_4, \text{HgSO}_4$** $\rightarrow$ **2-hexanone**（Markovnikov 水合得內部烯醇，互變異構化為單一**甲基酮**）。
  - **(f) 2 equiv $\text{HCl}$** $\rightarrow$ **2,2-dichlorohexane**（偕二氯代烷 geminal dichloride）。
- **Part B：不對稱內部炔 `2-hexyne`（兩端皆為內部 $sp$ 碳，親電加成／水合失去區域選擇性！）**
  - **(b) 1 equiv $\text{HBr}$** $\rightarrow$ **(Z)-2-bromo-2-hexene 與 (Z)-3-bromo-2-hexene 的混合物**（※注意：$\text{H}$ 與 $\text{Br}$ 為 *anti* 反式加成，因此高優先序的 $-\text{Br}$ 與對側的烷基 $-\text{R}$ 會在雙鍵**同側**，依 CIP 規則命名為 **Z**！）。
  - **(d) $\text{Li}$ in $\text{NH}_3$** $\rightarrow$ **trans-2-hexene [(E)-2-hexene]**（立體專一性 *anti* 還原）。
  - **(e) $\text{H}_2\text{O}, \text{H}_2\text{SO}_4, \text{HgSO}_4$** $\rightarrow$ **2-hexanone 與 3-hexanone 的混合物**（重要結論：只有「末端炔」或「對稱內部炔」水合才可得單一產物！）。
</details>

---

### - [ ] 4. Problem 9-36 (p. 286g) ⭐⭐ 【末端炔 8 向蜘蛛網轉換圖】
**題目重點**：從末端炔 $\text{R-C}\equiv\text{CH}$ 出發，寫出完成 p. 286g 蜘蛛網圖中 8 個轉換所需的試劑（部分需結合第 8 章反應分兩步完成）：
1. $\rightarrow \text{RCH}_2\text{CH}_3$
2. $\rightarrow \text{RCH=CH}_2$
3. $\rightarrow \text{RCH}_2\text{CHO}$
4. $\rightarrow \text{RCH(Cl)CH}_3$
5. $\rightarrow \text{RCH}_2\text{CH}_2\text{OH}$
6. $\rightarrow \text{R-C}\equiv\text{C-CH}_3$
7. $\rightarrow \text{RCOCH}_3$
8. $\rightarrow$ 2-alkyloxirane（末端環氧烷）

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **$\rightarrow \text{RCH}_2\text{CH}_3$**：`2 H2, Pd/C`
2. **$\rightarrow \text{RCH=CH}_2$**：`H2, Lindlar catalyst`
3. **$\rightarrow \text{RCH}_2\text{CHO}$（醛）**：`1. BH3, THF (or Sia2BH); 2. H2O2, OH⁻`（[`hydroboration-alkyne`](cards/hydroboration-alkyne.md)）
4. **$\rightarrow \text{RCH(Cl)CH}_3$（兩步）**：
   - Step 1: `H2, Lindlar catalyst`（先還原為烯類 $\text{RCH=CH}_2$）
   - Step 2: `HCl, ether`（對烯類做 Markovnikov 加成）
5. **$\rightarrow \text{RCH}_2\text{CH}_2\text{OH}$（兩步）**：
   - Step 1: `H2, Lindlar catalyst`（先還原為烯類 $\text{RCH=CH}_2$）
   - Step 2: `1. BH3, THF; 2. H2O2, OH⁻`（對烯類做 anti-Markovnikov 水合；或先將炔轉為醛再用 $\text{NaBH}_4$ 還原）
6. **$\rightarrow \text{R-C}\equiv\text{C-CH}_3$**：`1. NaNH2, NH3; 2. CH3I (or CH3Br)`
7. **$\rightarrow \text{RCOCH}_3$（甲基酮）**：`H2O, H2SO4, HgSO4`（[`hgso4-hydration`](cards/hgso4-hydration.md)）
8. **$\rightarrow$ 末端環氧烷（兩步）**：
   - Step 1: `H2, Lindlar catalyst`（先還原為烯類 $\text{RCH=CH}_2$）
   - Step 2: `mCPBA (R'CO3H)`（過氧酸環氧化）
</details>

---

### - [ ] 5. Problem 9-43 (p. 286i) ⭐⭐ 【氘同位素立體與位置標記】
**題目重點**：如何將氘（Deuterium, $\text{D}$）精準引入下列分子的指定位置與立體構型中？
- (a) `3-hexyne` $\rightarrow$ *(Z)*-3,4-dideuterio-3-hexene（兩個 D 同側 *cis*）
- (b) `3-hexyne` $\rightarrow$ *(E)*-3,4-dideuterio-3-hexene（兩個 D 異側 *trans*）
- (c) `1-pentyne` $\rightarrow$ $\text{CH}_3\text{CH}_2\text{CH}_2\text{C}\equiv\text{CD}$
- (d) $\text{PhC}\equiv\text{CH} \rightarrow \text{PhCD=CD}_2$

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **(a)** **$\text{D}_2$, Lindlar catalyst**（催化劑表面 *syn* 加成兩個 D）。
- **(b)** **$\text{Li}$, $\text{ND}_3(\text{l})$**（溶解金屬 *anti* 還原，兩個 D 來自液態氘代氨 $\text{ND}_3$ 的質子化步驟）。
- **(c)** **1. $\text{NaNH}_2, \text{NH}_3$；2. $\text{D}_2\text{O}$**（強鹼拔掉末端炔 $\text{H}^+$ 形成乙炔負離子 $\text{RC}\equiv\text{C:}^-$，再加 $\text{D}_2\text{O}$ 酸鹼中和接上 D）。
- **(d)** **結合 (c) + (a) 兩步法**：
  1. `1. NaNH2, NH3; 2. D2O`（先得到 $\text{PhC}\equiv\text{CD}$）
  2. `D2, Lindlar catalyst`（再加上兩個 D 得到 $\text{PhCD=CD}_2$）。
</details>

---

## 第三部分：關鍵反應機構與酸鹼／中間體觀念（5 題）

### - [ ] 6. Problem 9-19 (p. 286b) ⭐⭐ 【2 當量 HX 加成生成偕二鹵代烷機構】
**題目重點**：畫出 `1-pentyne` + $2\ \text{HCl} \rightarrow$ `2,2-dichloropentane` 的完整電子箭頭機構，並解釋為何第二個 $-\text{Cl}$ 必定接在已經有 $-\text{Cl}$ 的 C2 上，而不是 C1？

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **機構與區域選擇性原因**：
  1. **第一當量 $\text{HCl}$**：叁鍵質子化在末端 C1，形成二級乙烯基碳陽離子（優於極不穩定的一級乙烯基碳陽離子），$\text{Cl}^-$ 接在 C2 得到 `2-chloro-1-pentene`。
  2. **第二當量 $\text{HCl}$**：雙鍵再次質子化在末端 C1，使正電荷落在已經接有氯原子的 C2 上。雖然 $-\text{Cl}$ 有誘導拉電子效應，但**氯原子的孤對電子可以向下推與碳陽離子進行共振（Resonance stabilization）**：
     $$\text{R}-\stackrel{+}{\text{C}}(\text{Cl})-\text{CH}_3 \longleftrightarrow \text{R}-\text{C}(=\stackrel{+}{\text{Cl}})-\text{CH}_3$$
     第二個共振結構中每個原子都滿足八隅體（octet rule），比正電荷落在 C1 穩定太多！最後第二個 $\text{Cl}^-$ 攻擊 C2，生成偕二氯代烷 `2,2-dichloropentane`。
</details>

---

### - [ ] 7. Problem 9-21 & 9-25 (pp. 286c–286d) ⭐⭐⭐ 【酸催化烯醇—酮互變異構＆丙酮六氘交換機構】
**題目重點**：
1. **(9-21)** 畫出烯醇 $\text{R-C(OH)=CH}_2$ 在 $\text{H}_3\text{O}^+$ 催化下互變異構化（tautomerize）為甲基酮 $\text{R-CO-CH}_3$ 的兩步電子箭頭機構。
2. **(9-25)** 將丙酮（$\text{CH}_3\text{COCH}_3$）放入酸性重水（$\text{D}_3\text{O}^+/\text{D}_2\text{O}$）中，為何全部 6 個氫都會被換成氘變成 $\text{CD}_3\text{COCD}_3$？畫出機構說明。

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **酸催化 Enol $\rightarrow$ Ketone 標準兩步機構（9-21）**：
   - **Step 1（先 C-質子化）**：烯醇的 $-\text{OH}$ 孤對電子推下來形成 $\text{C=O}$ 雙鍵，同時 $\text{C=C}$ 的 $\pi$ 電子出去抓取 $\text{H}_3\text{O}^+$ 的質子接在末端碳（變成 $-\text{CH}_3$），生成共振穩定的質子化酮 $\text{R}-\text{C}(=\stackrel{+}{\text{O}}\text{H})-\text{CH}_3$。
   - **Step 2（後 O-去質子化）**：$\text{H}_2\text{O}$ 拔除 $=\stackrel{+}{\text{O}}\text{H}$ 上的質子，得到中性的酮 $\text{R}-\text{C(=O)}-\text{CH}_3$。
2. **丙酮在 $\text{D}_3\text{O}^+$ 中的氫—氘交換機構（9-25）**：
   - 因為酮與烯醇的互變異構化是**可逆平衡**！
   - **正向（Ketone $\rightarrow$ Enol，脫去 H）**：丙酮的氧先被 $\text{D}_3\text{O}^+$ 氘化形成 $\text{CH}_3-\text{C}(=\stackrel{+}{\text{O}}\text{D})-\text{CH}_3$，接著 $\text{D}_2\text{O}$ 拔除甲基上的一個 **$\text{H}^+$**，生成烯醇 $\text{CH}_2=\text{C(OD)CH}_3$。
   - **逆向（Enol $\rightarrow$ Ketone，接上 D）**：烯醇變回酮時，雙鍵 $=\text{CH}_2$ 從 $\text{D}_3\text{O}^+$ 抓到一個 **$\text{D}^+$**，再脫去氧上的 $\text{D}^+$，變成 $\text{CH}_2\text{D}-\text{C(=O)}-\text{CH}_3$。
   - 重複此可逆過程 6 次，兩邊 $\alpha$-碳上的 6 個 H 就全部被換成 D 了！
</details>

---

### - [ ] 8. Problem 9-22 & 9-23 (pp. 286c–286d) ⭐⭐⭐ 【液氨中鋰還原機構：為何兼具 Radical 與 Polar？】
**題目重點**：畫出 `2-pentyne` 與 $\text{Li} / \text{NH}_3(\text{l})$ 反應生成 *trans*-2-pentene 的完整四步電子箭頭機構（注意區分單電子魚鉤箭頭 $\rightharpoonup$ 與雙電子箭頭 $\rightarrow$），並說明是哪一步決定了 *trans* 立體化學？

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **完整四步機構（兼具 Radical 與 Polar 步驟）**：
  1. **Step 1（Radical，單電子轉移 SET，畫魚鉤單箭頭 $\rightharpoonup$）**：鋰原子（$\text{Li}\cdot$）將 1 個電子轉移給叁鍵，叁鍵一個 $\pi$ 鍵均裂，形成一端為碳自由基、一端為碳陰離子的**自由基陰離子（radical anion）**。
  2. **Step 2（Polar，酸鹼質子化，畫雙箭頭 $\rightarrow$）**：強鹼性的碳陰離子端用孤對電子從溶劑 $\text{NH}_3$ 拔取一個 $\text{H}^+$（脫去 $\text{NH}_2^-$），生成**乙烯基自由基（vinylic radical）**。
  3. **Step 3（Radical，第二次單電子轉移，畫單箭頭 $\rightharpoonup$）**：第二個 $\text{Li}\cdot$ 將 1 個電子給乙烯基自由基，形成**反式乙烯基碳陰離子（*trans*-vinylic anion）**。
     - ⭐ **立體化學關鍵**：乙烯基自由基可快速翻轉，接受電子變成乙烯基碳陰離子時，為了避開兩個烷基（甲基與乙基）與孤對電子之間的立體排斥，**兩個烷基必定排在雙鍵反側（*trans*）**！
  4. **Step 4（Polar，第二次質子化，畫雙箭頭 $\rightarrow$）**：反式乙烯基碳陰離子從 $\text{NH}_3$ 拔取第二個 $\text{H}^+$，構型保持得到 **trans-2-pentene**。
</details>

---

### - [ ] 9. Problem 9-29 (p. 286f) ⭐⭐⭐ 【末端炔 + Br2/H2O 生成溴代酮機構】
**題目重點**：苯乙炔（$\text{PhC}\equiv\text{CH}$）與 $\text{Br}_2 / \text{H}_2\text{O}$ 反應會生成 $\alpha$-溴代苯乙酮（$\text{PhCOCH}_2\text{Br}$）。推導此反應的機構，並說明它類比於烯類的哪個反應？

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **類比關係**：類比於第 8 章烯類的**鹵醇形成反應（Halohydrin formation）**，再加上第 9 章的**烯醇—酮互變異構化（keto–enol tautomerization）**。
- **機構三步驟**：
  1. **形成不飽和溴鎓離子**：$\text{PhC}\equiv\text{CH}$ 與 $\text{Br}_2$ 反應形成三元環狀溴鎓離子中間體。
  2. **水分子區域選擇性開環**：$\text{H}_2\text{O}$ 攻擊取代基較多且能被苯環共振穩定的內部碳（C1），打開三元環並去質子化，形成**溴代烯醇（$\text{Ph-C(OH)=CHBr}$）**。
  3. **互變異構化**：溴代烯醇在酸中經歷「C2 質子化、O 去質子化」，轉變為穩定的 $\alpha$-溴代酮 $\text{PhCOCH}_2\text{Br}$。
</details>

---

### - [ ] 10. Problem 9-56 & 9-57 (p. 286l) ⭐⭐⭐ 【去質子化鹼強度判斷＆乙烯基碳陽離子穩定度】
**題目重點**：
1. **(9-56)** 下列哪幾種鹼可以將 `1-butyne`（$\text{p}K_\text{a} \approx 25$）去質子化？
   (a) $\text{KOH}$、(b) $\text{Na}^+\ ^-\text{CH}_2\text{S(=O)CH}_3$、(c) $\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2\text{Li}$、(d) $\text{Na}^+\ ^-\text{CH}_2\text{COCH}_3$
2. **(9-57a)** 將下列三個環戊烯相關碳陽離子依穩定度**由低到高**排列：
   ① 孤立二級碳陽離子（正電荷在 C4）、② 丙烯基碳陽離子（allylic，正電荷在 C3）、③ 乙烯基碳陽離子（vinylic，正電荷在雙鍵碳 C1 上）。

<details>
<summary>💡 點擊展開答案與詳解</summary>

1. **9-56 答案**：**(b)** 與 **(c)** 可以；**(a)** 與 **(d)** 不行。
   - **解析**：只有當鹼的**共軛酸 $\text{p}K_\text{a} > 25$** 時，才能有效拔除末端炔的質子（$\text{p}K_\text{a} \approx 25$）：
     - (a) $\text{KOH}$ 共軛酸為 $\text{H}_2\text{O}$（$\text{p}K_\text{a} = 15.7 < 25$）$\rightarrow$ **不可**。
     - (b) DMSO 碳陰離子共軛酸為 DMSO（$\text{p}K_\text{a} \approx 35 > 25$）$\rightarrow$ **可以**。
     - (c) $n\text{-BuLi}$ 共軛酸為丁烷（$\text{p}K_\text{a} \approx 50 \gg 25$）$\rightarrow$ **可以**。
     - (d) 丙酮烯醇負離子共軛酸為丙酮（$\text{p}K_\text{a} \approx 19.3 < 25$）$\rightarrow$ **不可**。
2. **9-57(a) 碳陽離子穩定度排序**：
   - **③ 乙烯基碳陽離子（vinylic cation，最不穩定）$<$ ① 孤立二級碳陽離子 $<$ ② 丙烯基碳陽離子（allylic cation，最穩定）**。
   - **解析**：乙烯基碳陽離子的空軌域所在的碳為 $sp$ 混成（50% $s$ 特性，電負度高），極度排斥正電荷；而丙烯基碳陽離子（allylic）有鄰位 $\pi$ 鍵共振分散正電荷，因此最穩定。
</details>

---

## 第四部分：多步有機合成設計（3 題）

### - [ ] 11. Problem 9-40 (p. 286h) ⭐⭐⭐ 【從烯類經由炔類的多步合成】
**題目重點**：從苯乙烯（styrene, $\text{PhCH=CH}_2$）出發，設計多步合成路線製備：
1. $\text{PhCH}_2\text{CHO}$（苯乙醛）
2. *(E)*-1-phenyl-1-propene（反式-1-苯基-1-丙烯，$\text{PhCH=CHCH}_3$）

<details>
<summary>💡 點擊展開答案與詳解</summary>

**核心套路**：當題目要從「烯類」合成「醛／酮」或「延長碳鏈」，第一步永遠是先透過 **`1. Br2; 2. 2–3 NaNH2` 把烯類升級為末端炔**！
1. **合成 $\text{PhCH}_2\text{CHO}$（三步）**：
   - Step 1: `Br2, CH2Cl2` $\rightarrow \text{PhCH(Br)CH}_2\text{Br}$
   - Step 2: `3 NaNH2, NH3; then H3O+` $\rightarrow \text{PhC}\equiv\text{CH}$（苯乙炔）
   - Step 3: `1. BH3, THF (or Sia2BH); 2. H2O2, OH⁻` $\rightarrow \text{PhCH}_2\text{CHO}$（末端炔 anti-Markovnikov 水合得醛）。
2. **合成 *(E)*-$\text{PhCH=CHCH}_3$（四步）**：
   - Step 1 & 2: 同上，先製備苯乙炔 $\text{PhC}\equiv\text{CH}$
   - Step 3: `1. NaNH2, NH3; 2. CH3I` $\rightarrow \text{PhC}\equiv\text{CCH}_3$（甲基化延長 1 個碳）
   - Step 4: `Li, NH3(l)` $\rightarrow$ *(E)*-1-phenyl-1-propene（*anti* 還原得反式雙鍵）。
</details>

---

### - [ ] 12. Problem 9-42 (p. 286i) ⭐⭐⭐ 【由乙炔出發的碳鏈構築】
**題目重點**：僅以乙炔（acetylene, $\text{HC}\equiv\text{CH}$）與任何 $\le 4$ 碳的鹵代烷為碳源，合成下列化合物：
- (c) `4-methyl-1-pentene`（$(\text{CH}_3)_2\text{CHCH}_2\text{CH=CH}_2$）
- (d) `4-octanone`（$\text{CH}_3\text{CH}_2\text{CH}_2\text{COCH}_2\text{CH}_2\text{CH}_2\text{CH}_3$）
- (e) `hexanal`（$\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2\text{CH}_2\text{CHO}$）

<details>
<summary>💡 點擊展開答案與詳解</summary>

- **(c) 合成 `4-methyl-1-pentene`**：
  - 切斷點在 C2–C3 單鍵：由乙炔與四碳一級鹵代烷 **1-bromo-2-methylpropane**（$(\text{CH}_3)_2\text{CHCH}_2\text{Br}$，注意接 Br 的碳是一級碳，可順利進行 $\text{S}_\text{N}2$！）烷基化得 `4-methyl-1-pentyne`，再用 `H2, Lindlar catalyst` 還原得 `4-methyl-1-pentene`。
- **(d) 合成 `4-octanone`**：
  - 目標是對稱的 8 碳酮，由對稱內部炔 **4-octyne** 水合可得單一產物！
  - 步驟：乙炔先後兩次使用 `1. NaNH2, NH3; 2. CH3CH2CH2Br`（1-bromopropane）進行雙邊烷基化得到 `4-octyne`，再用 `H2O, H2SO4, HgSO4` 水合得 `4-octanone`。
- **(e) 合成 `hexanal`**：
  - 目標是 6 碳醛，由末端炔 **1-hexyne** 經硼氫化氧化可得！
  - 步驟：乙炔 + `1. NaNH2, NH3; 2. CH3(CH2)3Br`（1-bromobutane）得 `1-hexyne`，再用 `1. BH3, THF; 2. H2O2, OH⁻` 得 `hexanal`。
</details>

---

### - [ ] 13. Problem 9-49 (p. 286j) ⭐⭐⭐⭐ 【必考經典：順反烯類的立體構型反轉】
**題目重點**：沒有任何一步反應能直接把順式烯變反式烯，但可透過多步反應完成。請寫出下列構型反轉的完整步驟：
- (a) *trans*-5-decene $\rightarrow$ *cis*-5-decene
- (b) *cis*-5-decene $\rightarrow$ *trans*-5-decene

<details>
<summary>💡 點擊展開答案與詳解</summary>

**解題公式**：「先加 $\text{Br}_2 \rightarrow$ 再用 $2\ \text{NaNH}_2$ 消去成線性炔類（洗掉原本的順反記憶）$\rightarrow$ 最後用 Lindlar（得 *cis*）或 $\text{Li/NH}_3$（得 *trans*）重新賦予立體構型！」
- **(a) *trans*-5-decene $\rightarrow$ *cis*-5-decene**：
  1. `Br2, CH2Cl2` $\rightarrow$ 5,6-dibromodecane
  2. `2 NaNH2, NH3` $\rightarrow$ `5-decyne`
  3. **`H2, Lindlar catalyst`** $\rightarrow$ *cis*-5-decene。
- **(b) *cis*-5-decene $\rightarrow$ *trans*-5-decene**：
  1. `Br2, CH2Cl2` $\rightarrow$ 5,6-dibromodecane
  2. `2 NaNH2, NH3` $\rightarrow$ `5-decyne`
  3. **`Li, NH3(l)`** $\rightarrow$ *trans*-5-decene。
</details>

---

## 第五部分：結構決定與綜合壓軸題（2 題）

### - [ ] 14. Problem 9-34 (p. 286g) ⭐⭐⭐ 【由氧化斷裂產物反推炔類與烯炔】
**題目重點**：反推經 $\text{KMnO}_4$ 或 $\text{O}_3$ 氧化斷裂後得到下列產物的碳氫化合物結構：
- (a) $\text{CO}_2 + \text{CH}_3(\text{CH}_2)_5\text{CO}_2\text{H}$
- (c) $\text{HO}_2\text{C(CH}_2)_8\text{CO}_2\text{H}$
- (d) $\text{CH}_3\text{CHO} + \text{CH}_3\text{COCH}_2\text{CH}_2\text{CO}_2\text{H} + \text{CO}_2$
- (e) $\text{OHC(CH}_2)_4\text{COCO}_2\text{H} + \text{CO}_2$

<details>
<summary>💡 點擊展開答案與詳解</summary>

**關鍵分辨技巧**：在臭氧化（`1. O3; 2. Zn`）條件下，**雙鍵（C=C）斷裂會停在醛／酮**，而**叁鍵（C≡C）斷裂則直接變成羧酸（$\text{RCO}_2\text{H}$）與 $\text{CO}_2$（末端 $\equiv\text{CH}$）**！
- **(a)** **1-octyne**，$\text{CH}_3(\text{CH}_2)_5\text{C}\equiv\text{CH}$（或 1-octene 經 $\text{KMnO}_4$）。
- **(c)** **cyclodecyne**（十元環炔，或 cyclodecene）。
- **(d)** 產物同時有醛（$\text{CH}_3\text{CHO}$）、酮（$\text{CH}_3\text{CO}-$）與羧酸 $+\ \text{CO}_2$，代表分子內**同時有一個三取代雙鍵與一個末端叁鍵**！將醛與酮接回雙鍵、羧酸與 $\text{CO}_2$ 接回末端叁鍵，得到：**5-methyl-5-hepten-1-yne**（$\text{CH}_3\text{CH=C(CH}_3)\text{CH}_2\text{CH}_2\text{C}\equiv\text{CH}$）。
- **(e)** 單一碎片同時含醛基（$-\text{CHO}$）與 $\alpha$-酮酸（$-\text{COCO}_2\text{H}$）外加 $\text{CO}_2$，代表是一個六元環內雙鍵（切開變一端醛、一端酮），且雙鍵的酮端原本接著一個末端乙炔基 $-\text{C}\equiv\text{CH}$（切開變 $-\text{CO}_2\text{H} + \text{CO}_2$），故結構為 **1-ethynylcyclohexene**（1-乙炔基環己烯）！
</details>

---

### - [ ] 15. Problem 9-47 & 9-54 (pp. 286j–286k) ⭐⭐⭐⭐ 【雙星壓軸：$\text{C}_9\text{H}_{12}$ 異構物結構大解謎】
**題目重點**：這兩題的主角剛好都是分子式為 **$\text{C}_9\text{H}_{12}$**、且在 $\text{Pd/C}$ 催化下都吸收 **3 當量 $\text{H}_2$** 得到 **$\text{C}_9\text{H}_{18}$** 的未知碳氫化合物，但反應行為截然不同：
- **Case 1 (9-47)**：化合物 **A** ($\text{C}_9\text{H}_{12}$) 臭氧化得到 `cyclohexanone`（環己酮）等產物；且 **A** 與 `1. NaNH2, NH3; 2. CH3I` 反應可生成 **C** ($\text{C}_{10}\text{H}_{14}$)。求 **A、B、C**。
- **Case 2 (9-54)**：化合物 **A'** ($\text{C}_9\text{H}_{12}$) 與 $\text{H}_2\text{SO}_4 / \text{HgSO}_4$ 水合得到兩個酮異構物 **C'** 與 **D'**；若與 $\text{KMnO}_4$ 氧化則得到乙酸（$\text{CH}_3\text{CO}_2\text{H}$）與對稱三元羧酸 **E**（$\text{HO}_2\text{CCH}_2\text{CH(CH}_2\text{CO}_2\text{H)\text{CH}_2\text{CO}_2\text{H}}$）。求 **A'～D'**。

<details>
<summary>💡 點擊展開答案與詳解</summary>

**共同第一步（不飽和度 IHD 分析）**：
- $\text{C}_9\text{H}_{12}$ 的 $\text{IHD} = \frac{2(9)+2-12}{2} = \mathbf{4}$。
- 吸收 **3 當量 $\text{H}_2$** 變成 $\text{C}_9\text{H}_{18}$（$\text{IHD}=1$），代表兩者皆含有 **1 個環 + 3 個 $\pi$ 鍵（1 個叁鍵 + 1 個雙鍵）**！

- **Case 1 (9-47) 解析**：
  1. 能與 $\text{NaNH}_2/\text{CH}_3\text{I}$ 反應多一個碳 $\rightarrow$ 必含**末端炔（$-\text{C}\equiv\text{CH}$）**。
  2. 臭氧化給出 `cyclohexanone`（6 個碳）$\rightarrow$ 六元環上有一個**環外雙鍵**。
  3. 9 個碳扣掉六元環（6 C）與末端炔（2 C）只剩 1 個碳（$=\text{CH}-$），故環外雙鍵直接連著末端炔：
     - **A** = **(2-propynylidene)cyclohexane**（$\text{Cyclohexylidene-CH-C}\equiv\text{CH}$）
     - **B** = **propylcyclohexane**
     - **C** = **(2-butynylidene)cyclohexane**（末端接上甲基變成 $-\text{C}\equiv\text{C-CH}_3$）。

- **Case 2 (9-54) 解析**：
  1. 在 $\text{HgSO}_4/\text{H}_2\text{SO}_4$ 下水合得到**兩種酮異構物** $\rightarrow$ 必含一個**不對稱內部叁鍵**！
  2. $\text{KMnO}_4$ 氧化產物中有乙酸（$\text{CH}_3\text{CO}_2\text{H}$，2 個碳）$\rightarrow$ 該內部叁鍵必為 **1-丙炔基（$-\text{C}\equiv\text{C-CH}_3$）**！
  3. 另一個氧化產物 **E** 為對稱的三元羧酸 $\text{CH(CH}_2\text{CO}_2\text{H)}_2(\text{CO}_2\text{H})$：其中直接連在中間 $\text{CH}$ 上的 $-\text{CO}_2\text{H}$ 來自 $-\text{C}\equiv\text{C-CH}_3$ 的斷裂，而兩側對稱的 $-\text{CH}_2\text{CO}_2\text{H}$ 則來自**環己烯 C1=C2 雙鍵**的斷裂（取代基在 C4 位置才對稱！）：
     - **A'** = **4-(1-propynyl)cyclohexene**
     - **B'** = **propylcyclohexane**
     - **C' & D'** = 叁鍵水合所得的兩種位置異構酮：**1-(3-cyclohexenyl)-1-propanone** 與 **1-(3-cyclohexenyl)-2-propanone**。
</details>
