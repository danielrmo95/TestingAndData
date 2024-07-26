describe('User Registration', () => {
  beforeEach(() => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-in');
  });

  it('should login', () => {
    
    cy.get('#email').type('danielrmo95@gmail.com');
    cy.get('#password').type('Contrasena1');

    cy.contains('button', 'Sign in').click();
    cy.get('label.btn.btn-ghost.btn-circle.avatar').click();
    cy.contains('a', 'Logout').click();

  });
});




