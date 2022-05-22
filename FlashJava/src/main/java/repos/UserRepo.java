package repos;

import models.User;

import java.util.List;

public interface UserRepo {

    public User getUser(int userId);

    public List<User> getAllUsers();

    public User addUser(User u);

    public User updateUser(User change);

    public User deleteUser(int userId);

}
