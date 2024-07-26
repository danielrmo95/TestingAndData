describe('User Registration', () => {
  it('should validate that the full name field accepts at least 2 words', () => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-up');    
    cy.get('#full-name').type('Daniel');
    cy.get('#email').type('danielrmo95@gmail.com');
    cy.get('#password').type('Contrasena1.');
    cy.get('#confirm-password').type('Contrasena1.');
    
    //Valida que el botón no se habilite si la contraseña es incorrecta
    cy.get('button[type="submit"]').should('be.disabled');


  });
});
