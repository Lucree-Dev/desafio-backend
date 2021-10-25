<?php
namespace App\Service;

use App\Entity\Friend;
use App\Entity\Person as EntityPerson;
use App\Repository\FriendRepository;
use App\Repository\PersonRepository;

class Person 
{
    /** 
     * @var PersonRepository 
     * */
    private $repository;

    /** 
     * @var FriendRepository
     */
    private $friendRepository;

    public function __construct(PersonRepository $repo, FriendRepository $friendRepository)
    {
        $this->repository = $repo;
        $this->friendRepository = $friendRepository;
    }

    /**
     * 
     */
    public function list():array
    {
        return $this->repository->findAll();
    }

    /**
     * @var array $data
     * @return EntityPerson
     */
    public function create(array $data): EntityPerson
    {
        $birthDay = $data['birthday'];
        if (!$birthDay instanceof \DateTime) {
            $birthDay = \DateTime::createFromFormat('Y-m-d', $data['birthday']);
        }
        
        $person = new EntityPerson();
        $person
            ->setFirstName($data['first_name'])
            ->setLastName($data['last_name'])
            ->setBirthday($birthDay)
            ->setPassword($data['password'])
            ->setUsername($data['username'])
        ;
        return $this->repository->create($person);
    }

    public function get($id): EntityPerson
    {
        return $this->repository->find($id);
    }

    public function createFrienship(EntityPerson $person, EntityPerson $person2): Friend
    {
        $friend = new Friend();
        $friend->setPerson($person)->setFriend($person2);
        return $this->friendRepository->create($friend);
    }
}