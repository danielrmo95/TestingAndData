describe('User Registration', () => {
  beforeEach(() => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-in');
  });

  it('should login and show the user full name', () => {
    
    cy.get('#email').type('danielrmo95@gmail.com');
    cy.get('#password').type('Contrasena1');

    cy.contains('button', 'Sign in').click();

    cy.get('h2.font-bold').should('contain.text', 'Daniel Fernando Romero Ochoa');
  });

});




