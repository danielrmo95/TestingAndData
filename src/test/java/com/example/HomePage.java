package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class HomePage {

    private WebDriver driver;

    // Elementos
    private By originField = By.xpath("//label[contains(text(), 'Origen')]/following-sibling::div//input[@class='input-tag']");
    private By destinationField = By.xpath("//label[contains(text(), 'Destino')]/following-sibling::div//input[@class='input-tag']");
    private By searchButton = By.xpath("//button[./em[text()='Buscar']]"); 
    private By dateField = By.xpath("//label[contains(text(), 'Fechas')]/following-sibling::div//input[@class='input-tag']");
    private By datein = By.xpath("//div[contains(@class, 'sbox5-monthgrid-datenumber') and .//div[text()='15']]");
    private By datefi = By.xpath("//div[contains(@class, 'sbox5-monthgrid-datenumber') and .//div[text()='16']]");

    // Constructor
    public HomePage(WebDriver driver) {
        this.driver = driver;
    }

    // Métodos de la página
    public void setOrigin(String origin) throws InterruptedException {
        WebElement element = driver.findElement(originField);
        element.sendKeys(origin);
        Thread.sleep(2000); 
    }

    public void setDestination(String destination) throws InterruptedException {
        WebElement element = driver.findElement(destinationField);
        element.click();
        Thread.sleep(10000);
        element.sendKeys(destination);
        Thread.sleep(10000); 

    }

    public void selectDates() throws InterruptedException {
        WebElement dateFieldElement = driver.findElement(dateField);
        dateFieldElement.click();
        Thread.sleep(2000); 
        WebElement dateInElement = driver.findElement(datein);
        dateInElement.click();
        Thread.sleep(2000);
        WebElement dateFiElement = driver.findElement(datefi);
        dateFiElement.click();
        Thread.sleep(5000);
    }

    public void clickSearchButton() throws InterruptedException {
        WebElement button = driver.findElement(searchButton);
        button.click();
        Thread.sleep(10000);
    }
}
