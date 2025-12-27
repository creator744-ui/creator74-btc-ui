import React from 'react';

/**
 * WalletCard Component
 * Displays balances for BTC, USD, and DTX, including a caption about the conversion logic.
 */
const WalletCard: React.FC = () => {
    return (
        <div className="wallet-card">
            <h2>Wallet Balances</h2>
            <p>BTC Balance: <span id="btc-balance">0.00</span></p>
            <p>USD Balance: <span id="usd-balance">0.00</span></p>
            <p>DTX Balance: <span id="dtx-balance">0.00</span></p>
            <small>* Conversion logic for USD and DTX balances uses the latest BTC exchange rates.</small>
        </div>
    );
};

export default WalletCard;