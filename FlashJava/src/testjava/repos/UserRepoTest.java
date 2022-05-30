package repos;

import models.User;
import org.jetbrains.annotations.Nullable;
import org.junit.jupiter.api.Test;
import repos.UserRepo;
import repos.UserRepoImpl;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class UserRepoTest {
    UserRepo ur = new UserRepoImpl();

    @Test
    public void getUser()
    {
        int userId = 1;
        User actual = ur.getUser(userId);
        User expected = new User(1, "flash_user", "pwd1", "admin");

        assertEquals(expected, actual);

    };

    @Test
    public void allUser(){
        List<User> ul = ur.getAllUsers();
        assertTrue(ul.size() > 1);
    };

    @Test
    public void deleteUser() {
        assertNotNull(ur.deleteUser(4));
    };

    @Test
    public void createUser() {
        User u = new User();
        User actual = ur.addUser(u);
        User expected = new User(actual.getUserId(), "null", "null","null");
        assertEquals(expected.getUserId(), actual.getUserId());
    };

    @Test
    public void updateUser() {
        User u = ur.getUser(5);
        u.setUserRole("Card Maker");
        User actual = ur.updateUser(u);
        User expected = new User(actual.getUserId(), "null", "null","Card Maker");
        assertEquals(expected.getUserRole(),actual.getUserRole());

    }
}
