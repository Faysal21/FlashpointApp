package services;

import models.User;

import java.util.List;

public interface UserService {

    public User getUser(int userId);

    public List<User> getAllUsers();

    public User addUser(User u);

    public User updateUser(User change);

    public User deleteUser(int userId);


}
