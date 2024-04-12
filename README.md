# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> 1. **交易路徑**：tokenB -> tokenA -> tokenC -> tokenE -> tokenD -> tokenC -> tokenB
> 2. **每次交易的金額輸入與輸出**：
>     - tokenB -> tokenA
>     - amountIn = 5.000000
>     - amountOut = 5.666667
>   - tokenA -> tokenC
>     - amountIn = 5.666667
>     - amountOut = 2.380000
>   - tokenC -> tokenE
>     - amountIn = 2.380000
>     - amountOut = 1.537964
>   - tokenE -> tokenD
>     - amountIn = 1.537964
>     - amountOut = 3.477202
>   - tokenD -> tokenC
>     - amountIn = 3.477202
>     - amountOut = 6.739982
>   - tokenC -> tokenB
>     - amountIn = 6.739982
>     - amountOut = 22.592156
> 3. **最終獎勵**：final tokenB balance = 22.592156

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> **滑點**在自動化做市商（AMM）如Uniswap的背景中，指的是交易預期價格和實際執行價格之間的差異。這通常是由於交易提交和執行之間流動池中供需的變化所導致。

> Uniswap V2透過**恆定乘積公式**來解決滑點問題，該公式用 $x \times y = k$ 表示，其中 $x$ 和 $y$ 是流動池中兩種代幣的儲備，而 $k$ 是一個常數。當執行交易時，儲備的乘積必須保持不變，從而調整價格。

> **範例函數**：
> 假設你想在初始儲備為 $x = 1000$ ETH 和 $y = 200,000$ DAI 的池中用 ETH 換取 DAI。

> 如果你加入 $\Delta x = 1$ ETH：
> $(x + \Delta x) \times (y - \Delta y) = k$
> $(1000 + 1) \times (200,000 - \Delta y) = 200,000 \times 1000$
> 解方程找到 $\Delta y$，即收到的 DAI 數量，考慮到由於儲備比例變化導致的滑點影響。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> 在UniswapV2對的合約中，第一次鑄造流動性時，會永久鎖定最小流動性 $1000$ 代幣。這樣做是為了防止在池子剛創建時，有人擁有所有流動性代幣，從而完全控制池子的定價。最小流動性作為一種保護機制，防止操縱並且確保池子總是有一些流動性，可能提高穩定性。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> 在最初鑄造後的後續流動性存入時，根據池中現有儲備比率發行流動性代幣。使用的具體公式為：
> $\text{流動性} = \text{min}\left(\frac{\text{數量0} \times \text{總供應量}}{\text{儲備0}}, \frac{\text{數量1} \times \text{總供應量}}{\text{儲備1}}\right)$
> 這種設計的意圖是確保基於當前池儲備比率按比例發行流動性份額。這樣可以防止現有流動性提供者的份額被稀釋，並根據貢獻的資產相對市場價值公平地分配價值。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> **三明治攻擊**在基於AMM的去中心化交易所如Uniswap的背景中，涉及惡意交易者在一個普通用戶的待處理交易的兩邊下單。攻擊者看到一個用戶

> 試圖交換（例如）ETH為DAI的待處理交易，並在用戶的交易之前下一個使價格上升的訂單，以及在用戶的交易後立即賣出資產。

> 這對用戶的影響是，由於攻擊者的交易操縱價格上升，用戶收到的代幣數量少於預期。從本質上講，用戶成為由攻擊者的買入和賣出訂單形成的三明治中的“肉”，導致更高的滑點和更差的交易執行。
