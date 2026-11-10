import streamlit as st

st.set_page_config(page_title="Money + Bet App", page_icon="💵")
st.title("💵 Money + Bet App")
st.caption("Converter • Daily Income • Bet Calculator")

tab1, tab2, tab3 = st.tabs(["Converter", "Daily Income", "Bet Calc"])

with tab1:
    st.subheader("Naira ⇄ Dollar")
    amount = st.number_input("Amount", value=8500000.0)
    from_cur = st.selectbox("From", ["Naira (₦)", "Dollar ($)"])
    rate = st.number_input("Rate: 1 Dollar =", value=1374.0)
    if st.button("Convert"):
        result = amount / rate if "Naira" in from_cur else amount * rate
        sym = "$" if "Naira" in from_cur else "₦"
        st.success(f"Result: {sym}{result:,.2f}")
        st.write(f"Rate used: ₦{rate:,.2f} = $1")

with tab2:
    st.subheader("Daily Income")
    daily = st.number_input("How much do you make per day? ($)", value=6186.32)
    rate2 = st.number_input("Rate: 1 Dollar =", value=1374.0, key="rate2")
    if st.button("Calculate My Year"):
        st.write(f"Per Day: ${daily:,.2f} / ₦{daily*rate2:,.2f}")
        st.write(f"Per Week: ${daily*7:,.2f} / ₦{daily*7*rate2:,.2f}")
        st.write(f"Per Month: ${daily*30:,.2f} / ₦{daily*30*rate2:,.2f}")
        st.success(f"Per Year: ${daily*365:,.2f} / ₦{daily*365*rate2:,.2f}")

with tab3:
    st.subheader("Bet Calculator")
    stake = st.number_input("Stake ($) - How much you want to bet", value=1100000.0)
    odds = st.number_input("Odds (e.g. 1.50 or 10)", value=1.50)
    if st.button("Calculate Bet"):
        total = stake * odds
        profit = total - stake
        st.success(f"Total Return if you win: ${total:,.2f}")
        st.write(f"Your Profit: ${profit:,.2f}")
        st.error(f"If you lose: -${stake:,.2f}")
    st.caption("⚠️ If you lose, you lose your full stake.")