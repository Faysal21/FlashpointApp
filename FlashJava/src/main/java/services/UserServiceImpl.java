package services;

import models.User;
import repos.UserRepo;

import java.util.List;

public class UserServiceImpl implements UserService {

    private UserRepo ur;

    public UserServiceImpl(UserRepo ur) {
        this.ur = ur;
    }

    @Override
    public User getUser(int userId) {
        return ur.getUser(userId);
    }

    @Override
    public List<User> getAllUsers() {
        return ur.getAllUsers();
    }

    @Override
    public User addUser(User u) {
        return ur.addUser(u);
    }

    @Override
    public User updateUser(User change) {
        return ur.updateUser(change);
    }

    @Override
    public User deleteUser(int userId) {
        return ur.deleteUser(userId);
    }
}
