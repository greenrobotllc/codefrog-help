---
title: Windows Store Subscriptions
layout: help
---

# Windows Store Subscriptions

This guide explains how to purchase, manage, and troubleshoot subscriptions for CodeFrog on Windows through the Microsoft Store.

## Overview

CodeFrog on Windows uses Microsoft Store in-app purchases (IAP) for subscription management. This provides a secure, native Windows experience with automatic receipt validation and cross-device synchronization.

### How Windows Store Subscriptions Work

- **Native Integration**: Subscriptions are managed through Microsoft Store
- **Automatic Validation**: Microsoft Store handles receipt validation automatically
- **Cross-Device Sync**: Your subscription works across all your Windows devices
- **Secure Payments**: All payments are processed securely through Microsoft Store
- **Automatic Renewal**: Subscriptions renew automatically unless cancelled

## Subscription Management

### Purchasing a Subscription

1. **Open CodeFrog**
   - Launch CodeFrog from the Start menu or Microsoft Store

2. **Navigate to Subscription**
   - If you see a paywall screen, click "Subscribe" or "Purchase"
   - Or go to Settings → Account → Subscription

3. **Select a Plan**
   - CodeFrog will display available subscription options
   - Review pricing and features for each plan
   - Select the plan that fits your needs

4. **Complete Purchase**
   - Click "Purchase" or "Subscribe"
   - Microsoft Store purchase dialog will appear
   - Sign in with your Microsoft account if prompted
   - Confirm the purchase
   - Wait for the purchase to complete

5. **Verification**
   - CodeFrog will automatically verify your subscription
   - You should see a confirmation message
   - The app will unlock premium features immediately

### Checking Subscription Status

To check your current subscription status:

1. **In CodeFrog**
   - Go to Settings → Account
   - Your subscription status will be displayed
   - Active subscriptions show expiration date

2. **In Microsoft Store**
   - Open Microsoft Store app
   - Click your profile icon (top right)
   - Go to "My Library"
   - Find CodeFrog and check subscription status

3. **Online**
   - Visit https://account.microsoft.com/services
   - Sign in with your Microsoft account
   - View all your subscriptions and services

### Renewing a Subscription

Subscriptions renew automatically:

- **Automatic Renewal**: Your subscription will renew automatically before expiration
- **Payment Method**: Uses the payment method on file with your Microsoft account
- **Notification**: You'll receive an email before renewal
- **Cancellation**: You can cancel anytime (see below)

### Cancelling a Subscription

To cancel your subscription:

1. **Via Microsoft Store**
   - Open Microsoft Store app
   - Click your profile icon → "Payment and billing"
   - Find CodeFrog subscription
   - Click "Manage" or "Cancel"
   - Follow the cancellation steps

2. **Via Microsoft Account Website**
   - Visit https://account.microsoft.com/services
   - Sign in with your Microsoft account
   - Find CodeFrog subscription
   - Click "Manage" → "Cancel subscription"
   - Confirm cancellation

3. **Important Notes**
   - Cancellation takes effect at the end of your current billing period
   - You'll retain access until the subscription expires
   - No refunds are provided for the current billing period
   - You can resubscribe anytime

### Restoring Purchases

If you've purchased on another Windows device or reinstalled CodeFrog:

1. **Automatic Restoration**
   - CodeFrog automatically checks for existing subscriptions on launch
   - Your subscription should be restored automatically

2. **Manual Restoration**
   - Go to Settings → Account
   - Click "Restore Purchases" if available
   - CodeFrog will check Microsoft Store for your subscription

3. **Troubleshooting**
   - Ensure you're signed in with the same Microsoft account
   - Check that you're connected to the internet
   - Wait a few minutes and try again (sync can take time)

## Troubleshooting

### Purchase Failures

**Problem**: Purchase fails or doesn't complete

**Solutions**:
- **Check Internet Connection**: Ensure you have a stable internet connection
- **Verify Microsoft Account**: Make sure you're signed in to Microsoft Store
- **Check Payment Method**: Verify your payment method is valid in Microsoft Store
- **Try Again**: Wait a few minutes and attempt the purchase again
- **Restart CodeFrog**: Close and reopen the app, then try purchasing again
- **Check Store Status**: Visit https://status.microsoft.com to check if Store services are down

### Network Errors

**Problem**: "Network error occurred" during purchase

**Solutions**:
- **Check Internet**: Verify your internet connection is working
- **Firewall Settings**: Ensure Windows Firewall isn't blocking Microsoft Store
- **VPN Issues**: If using a VPN, try disabling it temporarily
- **Proxy Settings**: Check if proxy settings are interfering
- **Try Later**: Network issues may be temporary, try again in a few minutes

### Server Errors

**Problem**: "Server error occurred" during purchase

**Solutions**:
- **Microsoft Store Status**: Check if Microsoft Store services are experiencing issues
- **Wait and Retry**: Server errors are usually temporary, wait 5-10 minutes and try again
- **Contact Support**: If the issue persists, contact Microsoft Store support

### Subscription Not Recognized

**Problem**: CodeFrog doesn't recognize your subscription

**Solutions**:
- **Restore Purchases**: Go to Settings → Account → Restore Purchases
- **Check Microsoft Account**: Ensure you're using the same Microsoft account that purchased the subscription
- **Restart CodeFrog**: Close and reopen the app
- **Check Store**: Verify subscription is active in Microsoft Store
- **Wait for Sync**: Subscription sync can take a few minutes, wait and check again
- **Reinstall**: As a last resort, uninstall and reinstall CodeFrog (your subscription will be restored)

### Already Purchased Error

**Problem**: "Already purchased" message but subscription doesn't work

**Solutions**:
- **Restore Purchases**: Try restoring purchases in CodeFrog
- **Check Subscription Status**: Verify in Microsoft Store that subscription is active
- **Restart App**: Close and reopen CodeFrog
- **Contact Support**: If issue persists, contact CodeFrog support with your Microsoft account email

### Payment Method Issues

**Problem**: Payment method is declined or invalid

**Solutions**:
- **Update Payment Method**: Go to Microsoft Store → Payment and billing → Update payment method
- **Check Card**: Ensure your credit/debit card is valid and not expired
- **Contact Bank**: Verify your bank isn't blocking the transaction
- **Try Different Method**: Add a different payment method to your Microsoft account

## License Management

### Understanding Your License

CodeFrog uses Microsoft Store's license-based model:

- **Active License**: You have a valid, active subscription
- **Inactive License**: Your subscription has expired or been cancelled
- **License Sync**: Licenses sync automatically across your Windows devices

### Checking License Status

1. **In CodeFrog**
   - Settings → Account shows your license status
   - Active licenses show expiration date
   - Inactive licenses show when they expired

2. **Via Windows Store API**
   - CodeFrog automatically checks license status on launch
   - License status is cached for offline access
   - License is re-validated when online

### License Expiration

When your subscription expires:

- **Grace Period**: You may have a short grace period (varies by subscription)
- **Feature Access**: Premium features will be locked after expiration
- **Data Preservation**: Your projects and data are preserved
- **Resubscribe**: You can resubscribe anytime to regain access

## Network Error Handling

### Offline Scenarios

CodeFrog handles offline scenarios gracefully:

- **Cached License**: CodeFrog caches your license status for offline use
- **Automatic Revalidation**: License is re-validated when you come back online
- **Graceful Degradation**: App continues to work with cached license status

### Handling Network Interruptions

If network is interrupted during purchase:

- **Purchase State**: Microsoft Store maintains purchase state
- **Automatic Retry**: CodeFrog will retry verification when online
- **Manual Retry**: You can manually restore purchases when online

### Sync Delays

License sync can take time:

- **Initial Sync**: First-time sync may take 1-5 minutes
- **Cross-Device Sync**: Sync between devices can take 5-10 minutes
- **Be Patient**: Wait a few minutes and check again
- **Manual Refresh**: Try restoring purchases to force a refresh

## Common Questions

### Can I use my subscription on multiple Windows devices?

Yes! Your Microsoft Store subscription works across all Windows devices where you're signed in with the same Microsoft account.

### What happens if I cancel my subscription?

Your subscription remains active until the end of the current billing period. After expiration, premium features will be locked, but your projects and data are preserved.

### Can I get a refund?

Refunds are handled by Microsoft Store according to their refund policy. Contact Microsoft Store support for refund requests.

### How do I change my payment method?

Update your payment method in Microsoft Store:
1. Open Microsoft Store
2. Click your profile → Payment and billing
3. Update your payment method

### Why doesn't my subscription work after reinstalling?

Subscriptions are tied to your Microsoft account, not the installation. After reinstalling, CodeFrog should automatically detect your subscription. If not, use "Restore Purchases" in Settings → Account.

## Getting Help

If you're experiencing issues with your subscription:

1. **Check This Guide**: Review the troubleshooting section above
2. **Microsoft Store Support**: Contact Microsoft Store support for payment or account issues
3. **CodeFrog Support**: Contact CodeFrog support for app-specific subscription issues
4. **Community**: Check CodeFrog community forums for similar issues

## Next Steps

- [Windows Setup Guide](/help/windows/windows-setup) - Configure CodeFrog on Windows
- [Windows Troubleshooting](/help/windows/windows-troubleshooting) - Solve common Windows issues
- [Getting Started](/help/windows/getting-started) - Learn how to use CodeFrog

