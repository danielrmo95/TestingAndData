package com.example;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
    
public class Main {
    public static void main(String[] args) {
        // Configura WebDriverManager para Chrome
        WebDriverManager.chromedriver().setup();

        // Configura opciones de Chrome
        ChromeOptions options = new ChromeOptions();
        // Ruta al perfil de usuario de Chrome
        options.addArguments("user-data-dir=C:\\Users\\Daniel Romero\\Desktop\\fastapi-mysql-restapi\\User Data");
        options.addArguments("profile-directory=Default"); // Usa el perfil 'Default'

        // Inicializa el navegador con las opciones configuradas
        WebDriver driver = new ChromeDriver(options);

        // Abre una página web
        driver.get("https://www.despegar.com.co/");
        
        // Asegúrate de cerrar el navegador al final
        driver.quit();
    }
}
