<?php
namespace App\Service;

use App\Entity\Person as EntityPerson;
use App\Repository\PersonRepository;
use Doctrine\Common\Persistence\ObjectManager;

class Person 
{
    /** 
     * @var PersonRepository 
     * */
    private $repository;

    public function __construct(PersonRepository $repo)
    {
        
        $this->repository = $repo;
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

    public function get($id)
    {

    }
}