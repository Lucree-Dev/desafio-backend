<?php

namespace App\Repository;

use App\Entity\Fried;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @method Fried|null find($id, $lockMode = null, $lockVersion = null)
 * @method Fried|null findOneBy(array $criteria, array $orderBy = null)
 * @method Fried[]    findAll()
 * @method Fried[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class FriedRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Fried::class);
    }

    // /**
    //  * @return Fried[] Returns an array of Fried objects
    //  */
    /*
    public function findByExampleField($value)
    {
        return $this->createQueryBuilder('f')
            ->andWhere('f.exampleField = :val')
            ->setParameter('val', $value)
            ->orderBy('f.id', 'ASC')
            ->setMaxResults(10)
            ->getQuery()
            ->getResult()
        ;
    }
    */

    /*
    public function findOneBySomeField($value): ?Fried
    {
        return $this->createQueryBuilder('f')
            ->andWhere('f.exampleField = :val')
            ->setParameter('val', $value)
            ->getQuery()
            ->getOneOrNullResult()
        ;
    }
    */
}
