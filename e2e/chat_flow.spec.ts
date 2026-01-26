import { test, expect } from '@playwright/test';

test.describe('AI Book Features', () => {

  test('should load cinematic landing page', async ({ page }) => {
    await page.goto('/');
    // Check for 3D canvas presence
    await expect(page.locator('.canvas-container canvas')).toBeVisible();
    await expect(page.getByText('Start Learning 🚀')).toBeVisible();
  });

  test('chat widget should open and send message', async ({ page }) => {
    await page.goto('/docs/intro'); // Assuming intro doc exists
    // Open chat
    await page.click('.chat-toggle');
    await expect(page.locator('.chat-window')).toBeVisible();
    
    // Type and send
    await page.fill('input[placeholder="Ask about this page..."]', 'What is ROS 2?');
    await page.click('button:has-text("Send")');
    
    // Expect user message
    await expect(page.locator('.message.user')).toContainText('What is ROS 2?');
    // Expect loading or response
    // await expect(page.locator('.loading')).toBeVisible();
  });

  test('focus mode should toggle visibility', async ({ page }) => {
    await page.goto('/docs/intro');
    // Default: navbar visible
    await expect(page.locator('.navbar')).toBeVisible();
    
    // Click focus toggle
    await page.click('.focus-toggle');
    // Content should have focus-mode class or navbar hidden
    await expect(page.locator('body')).toHaveClass(/focus-mode/);
    await expect(page.locator('.navbar')).toBeHidden();
  });

});
